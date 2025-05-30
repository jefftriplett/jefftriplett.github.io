#!/usr/bin/env -S uv --quiet run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "bs4",
#     "httpx",
#     "pydantic",
#     "python-frontmatter",
#     "python-slugify",
#     "rich",
#     "typer",
# ]
# ///
from datetime import datetime
from pathlib import Path
from urllib.parse import parse_qs
from urllib.parse import urlparse

import frontmatter
import httpx
import typer
from bs4 import BeautifulSoup
from pydantic import BaseModel
from pydantic import ConfigDict
from rich import print
from slugify import slugify


class MusicInfo(BaseModel):
    model_config = ConfigDict(extra="allow")

    category: str = "Music"
    cover: str
    date: datetime = datetime.now()
    link: str
    title: str
    spotify_id: str = ""
    youtube_id: str = ""


def generate_filename(music_info: MusicInfo) -> str:
    date_str = music_info.date.strftime("%Y-%m-%d")
    slug = slugify(music_info.title)
    return f"{date_str}-{slug}.md"


def generate_frontmatter(music_info: MusicInfo) -> str:
    post = frontmatter.Post("")
    post.metadata = music_info.model_dump()
    return frontmatter.dumps(post)


def extract_spotify_info(url: str) -> MusicInfo:
    """Extract info from Spotify URLs"""
    # Extract Spotify ID from URL
    spotify_id = url.split("/")[-1].split("?")[0]

    with httpx.Client() as client:
        response = client.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

    # Extract title from og:title meta tag
    title_meta = soup.find("meta", property="og:title")
    title = title_meta["content"] if title_meta else "Unknown Title"

    # Extract cover image from og:image meta tag
    cover_meta = soup.find("meta", property="og:image")
    cover = cover_meta["content"] if cover_meta else ""

    return MusicInfo(cover=cover, link=url, title=title, spotify_id=spotify_id)


def extract_youtube_info(url: str) -> MusicInfo:
    """Extract info from YouTube URLs"""
    # Extract YouTube ID from URL
    parsed_url = urlparse(url)
    if "youtu.be" in parsed_url.netloc:
        youtube_id = parsed_url.path[1:]
    else:
        youtube_id = parse_qs(parsed_url.query).get("v", [""])[0]

    with httpx.Client() as client:
        response = client.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

    # Extract title from og:title meta tag
    title_meta = soup.find("meta", property="og:title")
    title = title_meta["content"] if title_meta else "Unknown Title"

    # Extract cover image from og:image meta tag
    cover_meta = soup.find("meta", property="og:image")
    cover = cover_meta["content"] if cover_meta else ""

    # Use maxresdefault for better quality if available
    if youtube_id and not cover:
        cover = f"https://i.ytimg.com/vi/{youtube_id}/maxresdefault.jpg"

    return MusicInfo(cover=cover, link=url, title=title, youtube_id=youtube_id)


def scrape_music_info(url: str) -> MusicInfo:
    """Route to appropriate scraper based on URL"""
    if "spotify.com" in url:
        return extract_spotify_info(url)
    elif "youtube.com" in url or "youtu.be" in url:
        return extract_youtube_info(url)
    else:
        raise ValueError(f"Unsupported music platform: {url}")


def main(urls: list[str]):
    output_dir = Path("_music")
    output_dir.mkdir(exist_ok=True)

    # Load existing music entries
    existing_music = {}
    filenames = Path("_music").glob("*.md")
    for filename in filenames:
        try:
            post = frontmatter.loads(filename.read_text())
            if "link" in post.metadata:
                music_info = MusicInfo(**post.metadata)
                existing_music[music_info.link] = music_info
        except Exception as e:
            print(f"[red]Error reading {filename}: {e}[/red]")

    for url in urls:
        if url not in existing_music:
            try:
                music_info = scrape_music_info(url)
                frontmatter_content = generate_frontmatter(music_info)

                filename = generate_filename(music_info)
                output_file = output_dir / filename
                output_file.write_text(f"{frontmatter_content}\n")

                print(f"[green]Music information saved to {output_file}[/green]")
            except Exception as e:
                print(f"[red]Error processing {url}: {e}[/red]")
        else:
            print(f"[yellow]URL already exists: {url}[/yellow]")


if __name__ == "__main__":
    typer.run(main)
