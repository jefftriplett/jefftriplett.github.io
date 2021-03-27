import frontmatter
import json
import typer

from datetime import datetime
from pathlib import Path
from pydantic import BaseModel, ValidationError
from slugify import slugify
from typing import List, Optional


class Post(BaseModel):
    author: Optional[str] = None
    category: Optional[str] = "Personal"
    date: Optional[datetime] = None
    image: Optional[str] = None
    layout: Optional[str] = "post"
    location: Optional[str] = "Home @ Lawrence, Kansas United States"
    tags: List[str] = []
    slug: Optional[str] = None
    title: str
    weather: Optional[str] = None


# class PostSchema(typesystem.Schema):
#     author = typesystem.String(allow_null=True)
#     category = typesystem.Choice(
#         choices=[
#             "Django",
#             "DjangoCon",
#             "Five for Friyay",
#             "Inspiration",
#             "Personal",
#             "Personal Goals",
#             "Productivity",
#             "Python",
#             "Sunday Morning Coffee Links",
#             "TIL",
#         ],
#         default="Personal",
#     )
#     date = typesystem.DateTime(allow_null=True)
#     image = typesystem.String(allow_null=True)
#     layout = typesystem.String(default="post")
#     location = typesystem.String(default="Home @ Lawrence, Kansas United States")
#     tags = typesystem.Array(items=typesystem.String(), allow_null=True)
#     title = typesystem.String()
#     weather = typesystem.String(allow_null=True)


app = typer.Typer()


def scan_files(folder: str):
    posts = sorted(Path(folder).glob("*.md"))
    for filename in posts:
        typer.secho(f"{filename}", fg="white")
        try:
            data = frontmatter.load(filename)
            post = Post(**data.metadata)
            slug = slugify(f"{post.title}")

            if post.date:
                destination = filename.parent.joinpath(
                    f"{post.date:%Y-%m-%d}-{slug}{filename.suffix}"
                )

            else:
                destination = filename.parent.joinpath(f"{slug}{filename.suffix}")

            if filename.name not in ["README.md"] and not filename.name.startswith("_"):
                if slug != post.slug:
                    data.metadata["slug"] = slug
                    filename.write_text(frontmatter.dumps(data))

                if not destination.exists():
                    typer.secho(f"\t{destination}", fg="yellow")
                    # filename.rename(destination)

        except ValidationError as e:
            typer.echo(e.json())


@app.command()
def demo():
    scan_files("_drafts")


@app.command()
def main(filename: str):
    try:
        data = frontmatter.load(filename)
        post = Post(**data.metadata)
        slug = slugify(f"{post.title}")
        typer.echo(f"{slug}")
        typer.echo("----")

    except ValidationError as e:
        typer.echo(e.json())


@app.command()
def rename(filename: str):
    path = Path(filename)
    try:
        data = frontmatter.load(filename)
        post = Post(**data.metadata)
        slug = slugify(f"{post.title}")

        destination_path = path.parent.joinpath(f"{slug}{path.suffix}")

        if path != destination_path:
            typer.echo("rename")

        typer.echo(json.dumps(data.metadata, indent=2))
        typer.echo("----")

    except ValidationError as e:
        typer.echo(e.json())


if __name__ == "__main__":
    app()
