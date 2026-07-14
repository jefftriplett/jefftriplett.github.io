#!/usr/bin/env -S uv --quiet run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "httpx",
#     "markdownify",
#     "python-dateutil",
#     "python-frontmatter",
#     "python-slugify",
#     "rich",
#     "typer",
# ]
# ///
"""Backfill micro.blog posts that are missing from ``_posts/``.

The microblog at https://micro.webology.dev is the source of truth for
``category: micro.blog`` posts. Some of them (notably the 2024 archive) were
never cross-posted into this repo, so the sitemap lists ~185 URLs with no local
file (see jefftriplett.com issue #18).

Source of truth is the full JSON Feed archive at
https://github.com/jefftriplett/microblog (``feed.json``, all 272 posts), rather
than scraping individual pages. For each feed item with no matching local file
(matched on date +- 1 day and a normalized slug prefix, the same tolerance the
Django-side audit uses), this writes a Jekyll file in the same frontmatter shape
as the existing micro.blog posts. Downstream, the Django ``content`` app imports
the new files via ``manage.py sync_pull``.

Examples:
    ./scripts/fetch-microblog.py --dry-run
    ./scripts/fetch-microblog.py --limit 5
    ./scripts/fetch-microblog.py --year 2024
"""

from __future__ import annotations

import re
from datetime import timezone
from pathlib import Path

import frontmatter
import httpx
import typer
import yaml
from dateutil.parser import parse as parse_date
from markdownify import markdownify
from rich import print
from slugify import slugify


def _represent_none(dumper, _):
    """Emit ``None`` as an empty scalar (``tags:``) rather than ``tags: null``."""
    return dumper.represent_scalar("tag:yaml.org,2002:null", "")


yaml.SafeDumper.add_representer(type(None), _represent_none)

FEED_URL = "https://raw.githubusercontent.com/jefftriplett/microblog/main/feed.json"
DEFAULT_LOCATION = "Home @ Lawrence, Kansas United States"
SLUG_MAX_LENGTH = 64
USER_AGENT = "fetch-microblog (jefftriplett.github.io)"

# /YYYY/MM/DD/slug/
_DATED_RE = re.compile(r"^/(\d{4})/(\d{2})/(\d{2})/([^/]+)/?$")
# Local Jekyll filename: YYYY-MM-DD-slug.md
_FILENAME_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$")

app = typer.Typer(add_completion=False, no_args_is_help=False)


def fetch_feed(client: httpx.Client, feed_url: str) -> list[dict]:
    """Return the archive feed items, newest first."""
    data = client.get(feed_url).raise_for_status().json()
    items = data.get("items", [])
    return sorted(items, key=lambda i: i.get("date_published", ""), reverse=True)


def existing_index(posts_dir: Path) -> list[tuple]:
    """Index local posts as ``(date, normalized_slug)`` for missing-detection.

    The slug comes from frontmatter when present (authoritative), else the
    filename stem after the date prefix.
    """
    index = []
    for path in sorted(posts_dir.glob("*.md")):
        match = _FILENAME_RE.match(path.name)
        if not match:
            continue
        year, month, day, stem = match.groups()
        try:
            post = frontmatter.load(path)
            slug = post.metadata.get("slug") or stem
        except Exception:
            slug = stem
        index.append((parse_date(f"{year}-{month}-{day}").date(), _norm(str(slug))))
    return index


def _norm(slug: str) -> str:
    """Normalize a slug to bare alphanumerics so ``django-chat`` == ``djangochat``."""
    return re.sub(r"[^a-z0-9]", "", slug.lower())


def _slug_matches(a: str, b: str) -> bool:
    a, b = _norm(a), _norm(b)
    return bool(a) and bool(b) and (a == b or a.startswith(b) or b.startswith(a))


def item_url_parts(item: dict) -> tuple | None:
    """Parse ``(date, url_slug)`` from a feed item's URL, or None if unexpected."""
    match = _DATED_RE.match(httpx.URL(item["url"]).path)
    if not match:
        return None
    year, month, day, slug = match.groups()
    return parse_date(f"{year}-{month}-{day}").date(), slug


def is_present(item_date, url_slug: str, index: list[tuple]) -> bool:
    """True if a local file already covers this post.

    micro.blog's URL date can differ from the stored (timezone-shifted) date by a
    day, and its published slug is often a truncation of the imported slug, so we
    allow a +-1 day window plus a normalized prefix relationship between slugs.
    """
    for file_date, slug in index:
        if abs((file_date - item_date).days) <= 1 and _slug_matches(slug, url_slug):
            return True
    return False


def covered_by_slug(item_date, slug: str, index: list[tuple]) -> bool:
    """True if an indexed file has the same normalized slug within +-1 day.

    This is the write-time duplicate guard. ``is_present`` compares against the
    *URL* slug (which micro.blog mangles by dropping digits/words, so it can miss
    an existing post); by the time we write we know the real slug we derived from
    the title, which equals the existing file's slug, so a same-day match here is
    reliable and prevents near-duplicate files dated a day apart.
    """
    normalized = _norm(slug)
    return any(abs((file_date - item_date).days) <= 1 and file_slug == normalized for file_date, file_slug in index)


def derive_title(body: str) -> tuple[str, str]:
    """Derive a title from body text for title-less micro.blog posts.

    Mirrors the existing archive: if the body opens with an H1 the heading
    becomes the title and is removed from the body; otherwise the first line
    becomes the title and stays in the body.
    """
    lines = body.split("\n")
    first = lines[0].strip() if lines else ""
    if first.startswith("# "):
        return first[2:].strip(), "\n".join(lines[1:]).lstrip("\n")
    return first, body


def build_post(item: dict) -> tuple[str, frontmatter.Post]:
    """Render a feed item into ``(filename, Post)`` in the micro.blog shape."""
    # Normalize to UTC for both the frontmatter date and the filename prefix,
    # matching the existing ``...T..:..:...000000Z`` micro.blog posts.
    utc = parse_date(item["date_published"]).astimezone(timezone.utc)
    body = markdownify(item.get("content_html", ""), heading_style="ATX").strip()

    # micro.blog status posts often have no title; derive one from the content.
    title = (item.get("title") or "").strip()
    if not title:
        title, body = derive_title(body)

    slug = slugify(title, max_length=SLUG_MAX_LENGTH, word_boundary=True) or slugify(item["url"])

    post = frontmatter.Post(
        body,
        category="micro.blog",
        date=f"{utc:%Y-%m-%dT%H:%M:%S}.000000Z",
        layout="post",
        location=DEFAULT_LOCATION,
        slug=slug,
        title=title,
        redirect_to=item["url"],
        tags=item.get("tags") or None,
    )
    return f"{utc:%Y-%m-%d}-{slug}.md", post


def dump_post(post: frontmatter.Post) -> str:
    """Serialize a post to Jekyll Markdown, matching the existing files' style.

    Uses ``sort_keys=False`` to keep the canonical field order, ``allow_unicode``
    so emoji stay literal, and a wide line so long titles aren't folded.
    """
    header = yaml.dump(
        dict(post.metadata),
        Dumper=yaml.SafeDumper,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=4096,
    )
    return f"---\n{header}---\n\n{post.content}\n"


@app.command()
def main(
    posts_dir: Path = typer.Option(Path("_posts"), help="Directory of Jekyll posts to write into."),
    feed_url: str = typer.Option(FEED_URL, help="JSON Feed archive URL."),
    limit: int = typer.Option(0, help="Only process the N most recent missing posts (0 = all)."),
    year: str = typer.Option("", help="Only backfill posts from this year."),
    dry_run: bool = typer.Option(False, help="Report what would be written without writing."),
):
    """Backfill missing micro.blog posts into ``posts_dir``."""
    if not posts_dir.is_dir():
        raise typer.BadParameter(f"{posts_dir} is not a directory (run from the repo root?)")

    with httpx.Client(headers={"User-Agent": USER_AGENT}, follow_redirects=True, timeout=30.0) as client:
        items = fetch_feed(client, feed_url)

    index = existing_index(posts_dir)

    missing = []
    for item in items:
        parts = item_url_parts(item)
        if parts is None:
            continue
        item_date, url_slug = parts
        if not is_present(item_date, url_slug, index):
            missing.append(item)

    if year:
        missing = [i for i in missing if i["date_published"][:4] == year]
    if limit:
        missing = missing[:limit]

    print(f"[bold]{len(items)}[/bold] feed posts | [bold]{len(index)}[/bold] local files | "
          f"[bold yellow]{len(missing)}[/bold yellow] candidate(s) to backfill")
    if not missing:
        return

    written = skipped = failed = 0
    for i, item in enumerate(missing, 1):
        try:
            filename, doc = build_post(item)
            target = posts_dir / filename
            doc_date = parse_date(filename[:10]).date()
            doc_slug = str(doc.metadata.get("slug", ""))
            label = f"[{i}/{len(missing)}] {filename}"

            if target.exists() or covered_by_slug(doc_date, doc_slug, index):
                # Already have this post (exact filename, or same slug +-1 day).
                print(f"  [dim]exists[/dim] {label}")
                skipped += 1
            elif dry_run:
                print(f"  [cyan]would write[/cyan] {label}")
                written += 1
            else:
                target.write_text(dump_post(doc), encoding="utf-8")
                # Track it so a later feed item can't write a same-slug duplicate.
                index.append((doc_date, _norm(doc_slug)))
                print(f"  [green]wrote[/green] {label}")
                written += 1
        except Exception as exc:  # noqa: BLE001 - keep going, report at the end
            print(f"  [red]error[/red] {item.get('url')}: {exc}")
            failed += 1

    verb = "would write" if dry_run else "wrote"
    print(f"\n[bold]{verb} {written}[/bold], skipped {skipped} (already present), failed {failed}")
    if written and not dry_run:
        print("Next: commit _posts/, then in the Django project run "
              "[bold]just manage sync_pull[/bold] to import into the database.")


if __name__ == "__main__":
    app()
