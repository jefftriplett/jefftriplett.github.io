#!/usr/bin/env -S uv --quiet run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "bs4",
#     "httpx",
#     "pydantic",
#     "python-frontmatter",
#     "rich",
#     "typer",
# ]
# ///
from pathlib import Path

import frontmatter
import httpx
import typer
from bs4 import BeautifulSoup
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


def main(filename: str):
    doc = Path(filename).read_text()
    post = frontmatter.loads(doc)
    url = post["link"]

    with httpx.Client() as client:
        response = client.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract cover from og:image meta tag
        image = soup.find("img", class_="real", itemprop="image").get("data-original")

        if not image.endswith(".webp"):
            image = f"{image}.webp"

        post["cover"] = image

        output = frontmatter.dumps(post)
        print(output)
        Path(filename).write_text(f"{output}\n")


if __name__ == "__main__":
    typer.run(main)
