#!/usr/bin/env -S uv --quiet run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "bs4",
#     "playwright",
#     "pydantic",
#     "python-frontmatter",
#     "rich",
#     "typer",
# ]
# ///
from pathlib import Path

import frontmatter
import typer
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
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


def fetch_html(url: str, wait_selector: str = 'meta[property="og:image"]') -> str:
    # Headed browser bypasses Cloudflare's JS challenge that blocks plain HTTP.
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_context().new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60_000)
        page.wait_for_selector(wait_selector, state="attached", timeout=120_000)
        html = page.content()
        browser.close()
        return html


def main(filenames: list[str]):
    for filename in filenames:
        doc = Path(filename).read_text()
        post = frontmatter.loads(doc)
        url = post["link"]

        soup = BeautifulSoup(fetch_html(url), "html.parser")
        image = soup.find("meta", property="og:image").get("content")
        post["cover"] = image

        output = frontmatter.dumps(post)
        print(output)
        Path(filename).write_text(f"{output}\n")


if __name__ == "__main__":
    typer.run(main)
