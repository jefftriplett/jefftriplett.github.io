import frontmatter
import json
import typer

from datetime import datetime
from pathlib import Path
from pydantic import BaseModel, ValidationError
from slugify import slugify
from typing import List, Optional
from urllib.parse import urlencode


class Post(BaseModel):
    author: Optional[str] = None
    category: Optional[str] = "Personal"
    date: Optional[datetime] = None
    image: Optional[str] = None
    layout: Optional[str] = "post"
    location: Optional[str] = "Home @ Lawrence, Kansas United States"
    tags: List[str] = None
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


@app.command()
def dump(filename: str):
    try:
        data = frontmatter.load(filename)
        post = Post(**data.metadata)
        slug = slugify(f"{post.title}")
        typer.echo(f"{slug}")
        typer.echo("----")

    except ValidationError as e:
        typer.echo(e.json())


@app.command()
def process(folder: str):
    posts = sorted(Path(folder).glob("*.md"))
    for filename in posts:
        typer.secho(f"{filename}", fg="white")
        try:
            data = frontmatter.load(filename)
            post = Post(**data.metadata)

            slug = slugify(f"{post.title}")
            if slug != post.slug:
                post.slug = slug

            data.metadata.update(**post.dict(exclude_none=True))

            if post.date:
                destination = filename.parent.joinpath(
                    f"{post.date:%Y-%m-%d}-{slug}{filename.suffix}"
                )

            else:
                destination = filename.parent.joinpath(f"{slug}{filename.suffix}")

            if not filename.name.startswith("_") and filename.name not in ["README.md"]:
                if filename != destination:
                    typer.echo(f"renaming: {filename} to: {destination}")
                    filename.rename(destination)
                    filename = Path(destination)

                filename.write_text(frontmatter.dumps(data))

        except ValidationError as e:
            typer.secho(e.json(), fg="red")


@app.command()
def update_opengraph_image(folder: str, debug: bool = False):
    filenames = Path(folder).glob("**/*.md")
    for filename in filenames:
        try:
            data = frontmatter.load(filename)
            # post = Post(**data.metadata)
            # slug = slugify(f"{post.title}")
            typer.echo(f"{data.metadata['title']}")
            query = {
                "atSymbol": "true",
                "author": "webology",
                "authorSize": "text-2xl",
                "style": "modern",
                "tags": ",".join(data.metadata.get("tags", [])),
                "title": data.metadata.get("title", ""),
                # "titleMargin": "-m-6",
            }
            query = urlencode(query)

            if debug:
                image_url = f"https://generator.opengraphimg.com/?{query}"
            else:
                image_url = f"https://generator.opengraphimg.com/view?{query}"

            data.metadata["image"] = image_url
            filename.write_text(frontmatter.dumps(data))

        except ValidationError as e:
            typer.echo(e.json())


if __name__ == "__main__":
    app()
