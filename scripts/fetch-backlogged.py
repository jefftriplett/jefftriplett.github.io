# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "bs4",
#     "httpx",
#     "pydantic",
#     "python-frontmatter",
#     "python-slugify",
#     "typer",
# ]
# ///
import typer
import httpx
from bs4 import BeautifulSoup
from pydantic import BaseModel
from datetime import datetime
import frontmatter
from pathlib import Path
from slugify import slugify

class GameInfo(BaseModel):
    category: str = "Games"
    cover: str
    date: datetime = datetime.now()
    link: str
    title: str

def scrape_game_info(url: str) -> GameInfo:
    with httpx.Client() as client:
        response = client.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

    # Extract title from og:title meta tag
    title_meta = soup.find('meta', property='og:title')
    title = title_meta['content'] if title_meta else "Unknown Title"

    # Remove the year from the title if present
    title = title.split('(')[0].strip()

    # Extract cover image from itemprop="image" meta tag
    cover_meta = soup.find('meta', attrs={'itemprop': 'image'})
    cover_img = cover_meta['content'] if cover_meta else ""

    return GameInfo(
        title=title,
        link=url,
        cover=cover_img
    )

def generate_frontmatter(game_info: GameInfo) -> str:
    post = frontmatter.Post("")
    post.metadata = game_info.dict()
    return frontmatter.dumps(post)

def generate_filename(game_info: GameInfo) -> str:
    date_str = game_info.date.strftime("%Y-%m-%d")
    slug = slugify(game_info.title)
    return f"{date_str}-{slug}.md"

def main(url: str):
    game_info = scrape_game_info(url)
    frontmatter_content = generate_frontmatter(game_info)

    filename = generate_filename(game_info)
    output_dir = Path("_games")
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / filename

    with output_file.open("w") as f:
        f.write(frontmatter_content)

    print(f"Game information saved to {output_file}")

if __name__ == "__main__":
    typer.run(main)
