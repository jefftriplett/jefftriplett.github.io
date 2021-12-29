import frontmatter
import os
import pytz
import typer

from datetime import datetime
from dateutil.parser import parse
from pathlib import Path
from pydantic import BaseModel, ValidationError, validator
from slugify import slugify
from typing import List, Optional
from urllib.parse import urlencode


DEFAULT_TZ = pytz.timezone("America/Chicago")


class FrontmatterModel(BaseModel):
    """
    Our base class for our default "Frontmatter" fields.
    """

    date: Optional[str]  # TODO: Parse/fix...
    layout: str
    permalink: Optional[str]
    published: Optional[bool]
    redirect_from: Optional[List[str]]
    redirect_to: Optional[str]  # via the jekyll-redirect-from plugin
    sitemap: Optional[bool]
    title: str

    class Config:
        extra = "allow"


class PageModel(FrontmatterModel):
    description: Optional[str]
    heading: Optional[str]
    layout: Optional[str]
    title: Optional[str]


class PostModel(FrontmatterModel):
    author: Optional[str] = None
    categories: Optional[List[str]]
    category: Optional[str] = "Personal"
    date: Optional[datetime] = None
    image: Optional[str] = None
    layout: Optional[str] = "post"
    # location: Optional[str] = "Home @ Lawrence, Kansas United States"
    location: Optional[str] = None
    redirect_to: Optional[str] = None
    slug: Optional[str] = None
    tags: Optional[List[str]]
    title: str
    weather: Optional[str] = None

    @validator("date", pre=True)
    def parse_date(cls, value):
        return parse(f"{value}").astimezone(DEFAULT_TZ)
        # if isinstance(f"{value}", str):
        #     return parse(f"{value}").astimezone(DEFAULT_TZ)
        # else:
        #     return value
        #     return value.astimezone(DEFAULT_TZ)


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
        post = PostModel(**data.metadata)
        slug = slugify(f"{post.title}")
        typer.echo(f"{slug}")
        typer.echo("----")

    except ValidationError as e:
        typer.echo(e.json())


@app.command()
def fix_redirect_to(folder: str):
    posts = sorted(Path(folder).glob("*.md"))
    for filename in posts:
        try:
            post = frontmatter.load(filename)
            if "link-out" in post.metadata:
                typer.secho(f"{filename}", fg="white")
                print(post.metadata["link-out"])
                post.metadata["redirect_to"] = post.metadata["link-out"]
                post.content = ""
                del post.metadata["link-out"]
                filename.write_text(frontmatter.dumps(post))

        except ValidationError as e:
            typer.secho(e.json(), fg="red")


@app.command()
def fmt(folder: str):
    filenames = sorted(Path(folder).glob("*.md"))
    for filename in filenames:
        try:
            post = frontmatter.loads(filename.read_text())
            data = PostModel(**post.metadata)
            post.metadata.update(data.dict(exclude_unset=True))
            filename.write_text(frontmatter.dumps(post) + os.linesep)

        except ValidationError as e:
            typer.secho(f"{filename}", fg="red")
            typer.echo(e.json())

        except Exception as e:
            typer.secho(f"{filename}::{e}", fg="red")


@app.command()
def process(folder: str, slug_max_length: int = 64):
    posts = sorted(Path(folder).glob("**/*.md"))
    for filename in posts:
        if filename.stem not in ["README"]:
            typer.secho(f"{filename}", fg="white")
            try:
                try:
                    data = frontmatter.load(filename)
                    if len(data.metadata) == 0:
                        data["title"] = filename.stem
                    post = PostModel(**data.metadata)

                except ValidationError as e:
                    typer.secho(e.json(), fg="red")
                    print(post.dict(exclude_none=True))
                    post = PostModel(**data.metadata)

                slug = slugify(
                    f"{post.title}", max_length=slug_max_length, word_boundary=True
                )

                if slug != post.slug:
                    post.slug = slug

                if "date" in post:
                    if isinstance(post["date"], str):
                        date = parse(post["date"]).astimezone(DEFAULT_TZ)
                    else:
                        date = post["date"].astimezone(DEFAULT_TZ)

                data.metadata.update(**post.dict(exclude_none=True))

                if post.date:
                    destination = filename.parent.joinpath(
                        f"{post.date:%Y-%m-%d}-{slug}{filename.suffix}"
                    )

                else:
                    destination = filename.parent.joinpath(f"{slug}{filename.suffix}")

                if not filename.name.startswith("_"):
                    if filename != destination:
                        typer.echo(f"renaming: {filename} to: {destination}")
                        filename.rename(destination)
                        filename = Path(destination)

                    filename.write_text(frontmatter.dumps(data) + os.linesep)

            except ValidationError as e:
                typer.secho(e.json(), fg="green")
                print(post.dict(exclude_none=True))


@app.command()
def update_opengraph_image(folder: str, debug: bool = False):
    filenames = Path(folder).glob("**/*.md")
    for filename in filenames:
        try:
            data = frontmatter.load(filename)
            # post = PostModel(**data.metadata)
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


@app.command()
def validate(folder: str):
    posts = sorted(Path(folder).glob("*.md"))
    for filename in posts:
        try:
            data = frontmatter.loads(filename.read_text())
            PostModel(**data.metadata)

        except ValidationError as e:
            typer.secho(f"{filename}", fg="red")
            typer.echo(e.json())

        except Exception as e:
            typer.secho(f"{filename}::{e}", fg="red")


if __name__ == "__main__":
    app()
