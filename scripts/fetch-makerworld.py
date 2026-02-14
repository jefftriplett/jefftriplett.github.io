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

import frontmatter
import httpx
import typer
from bs4 import BeautifulSoup
from pydantic import BaseModel
from pydantic import ConfigDict
from rich import print
from slugify import slugify


class PrintingInfo(BaseModel):
    model_config = ConfigDict(extra="allow")

    category: str = "Printing"
    cover: str
    date: datetime = datetime.now()
    link: str
    title: str


def generate_filename(printing_info: PrintingInfo) -> str:
    date_str = printing_info.date.strftime("%Y-%m-%d")
    slug = slugify(printing_info.title)
    return f"{date_str}-{slug}.md"


def generate_frontmatter(printing_info: PrintingInfo) -> str:
    post = frontmatter.Post("")
    post.metadata = printing_info.model_dump()
    return frontmatter.dumps(post)


def scrape_printing_info(url: str) -> PrintingInfo:
    with httpx.Client() as client:
        response = client.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

    # Extract title from og:title meta tag
    title_meta = soup.find("meta", property="og:title")
    title = title_meta["content"] if title_meta else "Unknown Title"

    # Remove the year from the title if present
    title = title.split("(")[0].strip()

    # Extract cover image from itemprop="image" meta tag
    cover_meta = soup.find("meta", attrs={"itemprop": "image"})
    cover_img = cover_meta["content"] if cover_meta else ""

    return PrintingInfo(cover=cover_img, link=url, title=title)


def main(urls: list[str]):
    output_dir = Path("_printings")
    output_dir.mkdir(exist_ok=True)

    printings = {}
    filenames = Path("_printings").glob("*.md")
    for filename in filenames:
        post = frontmatter.loads(filename.read_text())
        printing_info = PrintingInfo(**post.metadata)
        printings[printing_info.link] = printing_info

    for url in urls:
        if url not in printings:
            printing_info = scrape_printing_info(url)
            frontmatter_content = generate_frontmatter(printing_info)

            filename = generate_filename(printing_info)
            output_file = output_dir / filename
            output_file.write_text(f"{frontmatter_content}\n")

            print(f"Printing information saved to {output_file}")


if __name__ == "__main__":
    typer.run(main)
