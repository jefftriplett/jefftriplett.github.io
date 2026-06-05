#!/usr/bin/env -S uv --quiet run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "httpx",
#     "pydantic",
#     "python-frontmatter",
#     "rich",
#     "typer",
# ]
# ///
import os
from pathlib import Path
from urllib.parse import urlparse

import frontmatter
import httpx
import typer
from pydantic import BaseModel
from pydantic import ConfigDict
from rich import print


class FrontmatterInfo(BaseModel):
    model_config = ConfigDict(extra="allow")

    category: str = "Series"
    cover: str
    date: str
    link: str
    title: str


TRAKT_API = "https://api.trakt.tv"


def parse_trakt_url(url: str) -> tuple[str, str]:
    parts = urlparse(url).path.strip("/").split("/")
    return parts[0], parts[1]


def fetch_cover(media_type: str, slug: str, client_id: str) -> str:
    headers = {
        "Content-Type": "application/json",
        "trakt-api-version": "2",
        "trakt-api-key": client_id,
    }
    url = f"{TRAKT_API}/{media_type}/{slug}?extended=full,images"
    with httpx.Client() as client:
        response = client.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

    posters = data.get("images", {}).get("poster", [])
    if not posters:
        raise RuntimeError(f"No poster returned for {media_type}/{slug}")

    cover = posters[0]
    if not cover.startswith(("http://", "https://")):
        cover = f"https://{cover}"
    # Normalize to the historical CDN host + size used across the site.
    cover = cover.replace("//media.trakt.tv/", "//walter.trakt.tv/")
    cover = cover.replace("/posters/medium/", "/posters/thumb/")
    return cover


def main(filenames: list[str]):
    client_id = os.environ.get("TRAKT_CLIENT_ID")
    if not client_id:
        raise typer.BadParameter(
            "TRAKT_CLIENT_ID is not set. Copy .envrc.example to .envrc, "
            "fill in your Trakt API client id, and run `direnv allow`."
        )

    for filename in filenames:
        post = frontmatter.loads(Path(filename).read_text())
        media_type, slug = parse_trakt_url(post["link"])
        post["cover"] = fetch_cover(media_type, slug, client_id)

        output = frontmatter.dumps(post)
        print(output)
        Path(filename).write_text(f"{output}\n")


if __name__ == "__main__":
    typer.run(main)
