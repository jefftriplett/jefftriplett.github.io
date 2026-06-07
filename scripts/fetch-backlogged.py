#!/usr/bin/env -S uv --quiet run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "bs4",
#     "playwright",
#     "pydantic",
#     "python-frontmatter",
#     "python-slugify",
#     "rich",
#     "typer",
# ]
# ///
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

import frontmatter
import typer
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from pydantic import BaseModel
from pydantic import ConfigDict
from rich import print
from slugify import slugify

BASE_URL = "https://backloggd.com"


class GameInfo(BaseModel):
    model_config = ConfigDict(extra="allow")

    category: str = "Games"
    cover: str
    date: datetime = datetime.now()
    link: str
    title: str


def generate_filename(game_info: GameInfo) -> str:
    date_str = game_info.date.strftime("%Y-%m-%d")
    slug = slugify(game_info.title)
    return f"{date_str}-{slug}.md"


def generate_frontmatter(game_info: GameInfo) -> str:
    post = frontmatter.Post("")
    post.metadata = game_info.model_dump()
    return frontmatter.dumps(post)


def fetch_html(url: str, wait_selector: str = 'meta[property="og:title"]') -> str:
    # Headed browser bypasses Cloudflare's JS challenge that blocks plain HTTP.
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_context().new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60_000)
        page.wait_for_selector(wait_selector, state="attached", timeout=120_000)
        html = page.content()
        browser.close()
        return html


def scrape_game_info(url: str) -> GameInfo:
    soup = BeautifulSoup(fetch_html(url), "html.parser")

    # Extract title from og:title meta tag
    title_meta = soup.find("meta", property="og:title")
    title = title_meta["content"] if title_meta else "Unknown Title"

    # Remove the year from the title if present
    title = title.split("(")[0].strip()

    # Extract cover image from itemprop="image" meta tag
    cover_meta = soup.find("meta", attrs={"itemprop": "image"})
    cover_img = cover_meta["content"] if cover_meta else ""

    # DLC pages return the generic Backloggd banner — fall back to the
    # in-page hero image (lazy-loaded igdb URL).
    if "meta_banner" in cover_img:
        for img in soup.find_all("img"):
            candidate = img.get("data-src") or img.get("src") or ""
            if "images.igdb.com" in candidate:
                if candidate.startswith("//"):
                    candidate = "https:" + candidate
                cover_img = candidate
                break

    return GameInfo(cover=cover_img, link=url, title=title)


def scrape_profile_game_urls(profile_url: str) -> list[str]:
    soup = BeautifulSoup(
        fetch_html(profile_url, wait_selector='a.cover-link[href^="/games/"]'),
        "html.parser",
    )
    urls: list[str] = []
    seen: set[str] = set()
    for a in soup.select('a.cover-link[href^="/games/"]'):
        href = a.get("href", "")
        full = urljoin(BASE_URL, href)
        if not full.endswith("/"):
            full += "/"
        if full not in seen:
            seen.add(full)
            urls.append(full)
    return urls


def main(
    urls: list[str] = typer.Argument(None, help="Backloggd game URLs to fetch."),
    user: str = typer.Option(
        None,
        "--user",
        "-u",
        help="Backloggd username — pull recent games from their profile.",
    ),
    limit: int = typer.Option(
        0,
        "--limit",
        "-n",
        help="Stop after fetching this many new entries (0 = no limit).",
    ),
):
    output_dir = Path("_games")
    output_dir.mkdir(exist_ok=True)

    games = {}
    filenames = Path("_games").glob("*.md")
    for filename in filenames:
        post = frontmatter.loads(filename.read_text())
        game_info = GameInfo(**post.metadata)
        games[game_info.link] = game_info

    targets: list[str] = list(urls or [])
    if user:
        profile_url = f"{BASE_URL}/u/{user}/games/"
        print(f"Scraping profile: {profile_url}")
        targets.extend(scrape_profile_game_urls(profile_url))

    if not targets:
        print("[yellow]No URLs to process. Pass game URLs or --user USERNAME.[/]")
        raise typer.Exit(code=1)

    added = 0
    for url in targets:
        if url in games:
            continue

        game_info = scrape_game_info(url)
        frontmatter_content = generate_frontmatter(game_info)

        filename = generate_filename(game_info)
        output_file = output_dir / filename
        output_file.write_text(f"{frontmatter_content}\n")

        games[url] = game_info
        added += 1
        print(f"Game information saved to {output_file}")

        if limit and added >= limit:
            print(f"[cyan]Reached --limit {limit}, stopping.[/]")
            break

    print(f"[green]Done. Added {added} new game(s).[/]")


if __name__ == "__main__":
    typer.run(main)
