import os
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode

import frontmatter
import pytz
import typer
from dateutil.parser import parse
from pydantic import BaseModel
from pydantic import field_validator
from pydantic import ValidationError
from rich import print
from slugify import slugify


DEFAULT_TZ = pytz.timezone("America/Chicago")
SLUG_MAX_LENGTH = 64


class FrontmatterModel(BaseModel):
    """
    Our base class for our default "Frontmatter" fields.
    """

    date: str | None = None  # TODO: Parse/fix...
    layout: str
    permalink: str | None = None
    published: bool | None = None
    redirect_from: list[str] | None = None
    redirect_to: str | None = None  # via the jekyll-redirect-from plugin
    sitemap: bool | None = None
    title: str

    class Config:
        extra = "allow"


class PageModel(FrontmatterModel):
    description: str | None = None
    heading: str | None = None
    layout: str | None = None
    title: str | None = None


class PostModel(FrontmatterModel):
    author: str | None = None
    categories: list[str] | None = None
    category: str | None = "Personal"
    date: datetime | None = None
    image: str | None = None
    layout: str | None = "post"
    # location: Optional[str] = "Home @ Lawrence, Kansas United States"
    location: str | None = None
    redirect_to: str | None = None
    slug: str | None = None
    tags: list[str] | None = None
    title: str
    weather: str | None = None

    @field_validator("date")
    def validate_date(cls, value):
        return parse(f"{value}").replace(microsecond=0).astimezone(DEFAULT_TZ)
        # if isinstance(f"{value}", str):
        #     return parse(f"{value}").astimezone(DEFAULT_TZ)
        # else:
        #     return value
        #     return value.astimezone(DEFAULT_TZ)


class ProjectModel(FrontmatterModel):
    archived: bool | None = False
    github: str | None = None
    homepage: str | None = None
    layout: str | None = None
    slug: str | None = None
    title: str | None = None


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
def draft(
    title: str,
    category: str = "Personal",
    layout: str = "post",
    location: str = "Home @ Lawrence, Kansas United States",
    overwrite: bool = False,
):
    slug = slugify(f"{title}", max_length=SLUG_MAX_LENGTH, word_boundary=True)

    filename = Path("_drafts", f"{slug}.md")
    template = Path("_drafts", "_draft-template.md")

    if template.exist():
        template = template.read_text()
    else:
        template = ""

    post = frontmatter.loads(template)
    post["category"] = category
    post["layout"] = layout
    post["location"] = location
    post["slug"] = slug
    post["title"] = title

    data = PostModel(**post.metadata)
    post.metadata.update(data.dict(exclude_unset=True))

    if overwrite or not filename.exists():
        filename.write_text(frontmatter.dumps(post))


@app.command()
def publish(filename: Path, overwrite: bool = False):
    if str(filename.parent) in ["_drafts"]:
        doc = frontmatter.load(filename)
        doc["date"] = datetime.now().replace(microsecond=0).astimezone(DEFAULT_TZ)
        post = PostModel(**doc.metadata)
        doc.metadata.update(post.dict(exclude_unset=True))
        destination = Path("_posts", f"{post.date:%Y-%m-%d}-{filename.name}")
        if overwrite or not destination.exists():
            filename.rename(destination).write_text(f"{frontmatter.dumps(doc)}\n")
            print(f"[yellow]{destination}[/yellow] was published")
        else:
            print(f"[red]{destination}[/red] already exists")


@app.command()
def dump(filename: str):
    try:
        data = frontmatter.load(filename)
        post = PostModel(**data.metadata)
        slug = slugify(f"{post.title}", max_length=SLUG_MAX_LENGTH, word_boundary=True)
        print(f"{slug}")
        print("----")

    except ValidationError as e:
        print(e.json())


@app.command()
def fix_redirect_to(folder: Path):
    posts = sorted(Path(folder).glob("*.md"))
    for filename in posts:
        try:
            post = frontmatter.load(filename)
            if "link-out" in post.metadata:
                print(f"{filename}")
                print(post.metadata["link-out"])
                post.metadata["redirect_to"] = post.metadata["link-out"]
                post.content = ""
                del post.metadata["link-out"]
                filename.write_text(frontmatter.dumps(post))

        except ValidationError as e:
            print(e.json())


@app.command()
def fmt(folder: Path):
    filenames = sorted(Path(folder).glob("*.md"))
    for filename in filenames:
        try:
            post = frontmatter.loads(filename.read_text())
            data = PostModel(**post.metadata)
            post.metadata.update(data.dict(exclude_unset=True))
            filename.write_text(frontmatter.dumps(post) + os.linesep)

        except ValidationError as e:
            print(f"[red]{filename}[/red]")
            print(e.json())

        except Exception as e:
            print(f"[red]{filename}[/red]")
            print(e)


@app.command()
def process(folder: Path):
    posts = sorted(Path(folder).glob("**/*.md"))
    for filename in posts:
        if filename.stem not in ["README"]:
            print(f"{filename}")
            try:
                try:
                    data = frontmatter.load(filename)
                    if len(data.metadata) == 0:
                        data["title"] = filename.stem
                    post = PostModel(**data.metadata)

                except ValidationError as e:
                    print(e.json())
                    print(post.dict(exclude_none=True))
                    post = PostModel(**data.metadata)

                slug = slugify(
                    f"{post.title}", max_length=SLUG_MAX_LENGTH, word_boundary=True
                )

                if slug != post.slug:
                    post.slug = slug

                if "date" in post:
                    if isinstance(post["date"], str):
                        date = (
                            parse(post["date"])
                            .replace(microsecond=0)
                            .astimezone(DEFAULT_TZ)
                        )
                    else:
                        date = (
                            post["date"].replace(microsecond=0).astimezone(DEFAULT_TZ)
                        )

                data.metadata.update(**post.dict(exclude_none=True))

                if post.date:
                    destination = filename.parent.joinpath(
                        f"{post.date:%Y-%m-%d}-{slug}{filename.suffix}"
                    )

                else:
                    destination = filename.parent.joinpath(f"{slug}{filename.suffix}")

                if not filename.name.startswith("_"):
                    if filename != destination:
                        print(f"renaming: {filename} to: {destination}")
                        filename.rename(destination)
                        filename = Path(destination)

                    filename.write_text(frontmatter.dumps(data) + os.linesep)

            except ValidationError as e:
                print(e.json())
                print(post.dict(exclude_none=True))


@app.command()
def projects():
    posts = sorted(Path("_projects").glob("**/*.md"))
    for filename in posts:
        print(f"{filename}")
        try:
            try:
                data = frontmatter.load(filename)
                if len(data.metadata) == 0:
                    data["title"] = filename.stem
                post = ProjectModel(**data.metadata)

            except ValidationError as e:
                print(e.json())
                print(post.dict(exclude_none=True))
                post = ProjectModel(**data.metadata)

            slug = slugify(
                f"{post.title}", max_length=SLUG_MAX_LENGTH, word_boundary=True
            )

            if slug != post.slug:
                post.slug = slug

            # if "date" in post:
            #     if isinstance(post["date"], str):
            #         date = parse(post["date"]).astimezone(DEFAULT_TZ)
            #     else:
            #         date = post["date"].astimezone(DEFAULT_TZ)

            data.metadata.update(**post.dict(exclude_none=True))

            destination = filename.parent.joinpath(f"{slug}{filename.suffix}")

            if not filename.name.startswith("_"):
                if filename != destination:
                    print(f"renaming: {filename} to: {destination}")
                    filename.rename(destination)
                    filename = Path(destination)

                filename.write_text(frontmatter.dumps(data) + os.linesep)

        except ValidationError as e:
            print(e.json())
            print(post.dict(exclude_none=True))


@app.command()
def update_opengraph_image(folder: Path, debug: bool = False):
    filenames = Path(folder).glob("**/*.md")
    for filename in filenames:
        try:
            data = frontmatter.load(filename)
            # post = PostModel(**data.metadata)
            # slug = slugify(f"{post.title}")
            print(f"{data.metadata['title']}")
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
            print(e.json())


@app.command()
def validate(folder: Path):
    posts = sorted(Path(folder).glob("*.md"))
    for filename in posts:
        try:
            data = frontmatter.loads(filename.read_text())
            PostModel(**data.metadata)

        except ValidationError as e:
            print(f"[red]{filename}[/red]")
            print(e.json())

        except Exception as e:
            print(f"[red]{filename}[/red]")
            print(e)


if __name__ == "__main__":
    app()
