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


class ProductInfo(BaseModel):
    model_config = ConfigDict(extra="allow")

    category: str = "Products"
    cover: str
    date: datetime = datetime.now()
    link: str
    title: str


def generate_filename(product_info: ProductInfo) -> str:
    date_str = product_info.date.strftime("%Y-%m-%d")
    slug = slugify(product_info.title)
    return f"{date_str}-{slug}.md"


def generate_frontmatter(product_info: ProductInfo) -> str:
    post = frontmatter.Post("")
    post.metadata = product_info.model_dump()
    return frontmatter.dumps(post)


def scrape_product_info(url: str) -> ProductInfo:
    with httpx.Client() as client:
        response = client.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

    # Extract title from og:title meta tag
    title_meta = soup.find("meta", property="og:title")
    title = title_meta["content"] if title_meta else "Unknown Title"

    # Remove common suffixes from the title if present
    title = title.split(" - ")[0].strip()
    title = title.split(" | ")[0].strip()
    title = title.split("(")[0].strip()

    # Extract cover image from og:image meta tag first, fallback to itemprop="image"
    cover_meta = soup.find("meta", property="og:image")
    if not cover_meta:
        cover_meta = soup.find("meta", attrs={"itemprop": "image"})
    
    cover_img = cover_meta["content"] if cover_meta else ""

    return ProductInfo(cover=cover_img, link=url, title=title)


def main(urls: list[str]):
    output_dir = Path("_products")
    output_dir.mkdir(exist_ok=True)

    # Load existing products
    existing_products = {}
    filenames = Path("_products").glob("*.md")
    for filename in filenames:
        try:
            post = frontmatter.loads(filename.read_text())
            if "link" in post.metadata:
                product_info = ProductInfo(**post.metadata)
                existing_products[product_info.link] = product_info
        except Exception as e:
            print(f"[red]Error reading {filename}: {e}[/red]")

    for url in urls:
        if url not in existing_products:
            try:
                product_info = scrape_product_info(url)
                frontmatter_content = generate_frontmatter(product_info)

                filename = generate_filename(product_info)
                output_file = output_dir / filename
                output_file.write_text(f"{frontmatter_content}\n")

                print(f"[green]Product information saved to {output_file}[/green]")
            except Exception as e:
                print(f"[red]Error processing {url}: {e}[/red]")
        else:
            print(f"[yellow]URL already exists: {url}[/yellow]")


if __name__ == "__main__":
    typer.run(main)