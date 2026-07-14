---
category: micro.blog
date: '2024-03-07T03:54:11.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: importing-data-with-django-ninja-s-modelschema
title: Importing data with Django Ninja's ModelSchema
redirect_to: https://micro.webology.dev/2024/03/06/importing-data-with-django-ninjas/
tags:
- Django
- Python
---

I have recently been playing with [Django Ninja](https://github.com/vitalik/django-ninja) for small APIs and for leveraging Schema. Specifically, [ModelSchema](https://django-ninja.dev/guides/response/django-pydantic/) is worth checking out because it’s a hidden gem for working with Django models, even if you aren’t interested in building a Rest API.

> Schemas are very useful to define your validation rules and responses, but sometimes you need to reflect your database models into schemas and keep changes in sync.
> <https://django-ninja.dev/guides/response/django-pydantic/>

One challenge we face is importing data from one legacy database into a new database with a different structure. While we can map old fields to new fields using a Python dictionary, we also need more control over what the data looks like coming back out.

Thankfully, ModelSchema is built on top of [Pydantic](%5BPydantic%5D(https://docs.pydantic.dev/latest/))’s [BaseModel](https://docs.pydantic.dev/2.6/api/base_model/) and supports Pydantic’s [Field alias](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) feature.

This allows us to create a ModelSchema based on a LegacyCategory model, and we can build out `Field(alias="...")` types to change the shape of how the data is returned.

We can then store the result as a Python dictionary and insert it into our new model. We can also log a JSON representation of the instance to make debugging easier. See [Serializing Outside of Views](https://django-ninja.dev/guides/response/#serializing-outside-of-views) for an overview of how the `from_orm` API works.

To test this, I built a proof of concept Django management command using [django-click](https://github.com/GaretJax/django-click), which loops through all our legacy category models and prints them.

```
# management/commands/demo_model_schema.py
import djclick as click

from ninja import ModelSchema
from pydantic import Field

from legacy.models import LegacyCategory
from future.models import Category


class LegacyCategorySchema(ModelSchema):
    name: str = Field(alias="cat_name")
    description: str = Field(alias="cat_description")
    active: bool = Field(alias="cat_is_active")

    class Meta:
        fields = ["id"]
        model = Category


@click.command()
def main():
    categories = LegacyCategory.objects.all()
    for category in categories:
        data = LegacyCategorySchema.from_orm(category).dict()
        print(data)
        # save to a database or do something useful here
```

## More resources

If you are curious about what Django Ninja is about, I recommend starting with their [CRUD example: Final Code](https://django-ninja.dev/tutorial/other/crud/#final-code), and working backward. This will give you a good idea of what a finished CRUD Rest API looks like with Django Ninja.
