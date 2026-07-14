---
category: micro.blog
date: '2024-02-19T22:58:37.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: django-ninja
title: 🥷 Django Ninja
redirect_to: https://micro.webology.dev/2024/02/19/django-ninja/
tags:
- Django
- Python
---

I have heard good things about [Django Ninja](https://django-ninja.dev), and I was looking for an excuse to try it out.

One pain point is syncing production data to a local Django development website. Most of the time, I can dump a database and restore it locally. Sometimes, creating a REST endpoint and creating a local Django management command to consume that input is easier.

That’s what my example is doing here with Django Ninja.

## `schemas.py`

If you have used [Django REST framework](https://www.django-rest-framework.org)’s [ModelSerializer](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer) before, you will feel at home with Django Ninja’s [ModelSchema](https://django-ninja.dev/guides/response/django-pydantic/#modelschema).

A ModelSchema class can generate a schema from a Django model and only needs to know which Django model and which fields you want to be exposed to your endpoint.

```
from ninja import ModelSchema

from places.models import Place


class PlaceSchema(ModelSchema):
    class Meta:
        model = Place
        fields = [
            "name",
            "slug",
            "active",
            "place_id",
            "address",
            ...
        ]
```

## `views.py`

Our Django Ninja view is going to going to query our database and return all of the active records in our `Place` model with respect to their creation date. Django Ninja will do the heavy lifting for us and apply our `PlaceSchema` which will return JSON data.

```
from ninja import Router
from ninja.pagination import LimitOffsetPagination
from ninja.pagination import paginate

from places.models import Place
from places.schemas import PlaceSchema


router = Router()


@router.get("/places/", response={200: list[PlaceSchema]})
@paginate(LimitOffsetPagination)
def list_places(request):
    qs = Place.objects.active().order_by("-created")
    return qs
```

## `routers.py`

This `routers.py` file is optional, but I prefer to keep my routers separate from my `urls.py`, and this felt cleaner. I would keep this code for a small app in my `urls.py` instead.

```
from ninja import NinjaAPI

from places.views import router as places_router

# API setup
api = NinjaAPI(csrf=True, version="1.0.0")
api.add_router("", places_router)
```

## `urls.py`

Our `urls.py` file is where we expose our router to the Internet so that our `/apis/places/` URI will be accessible to anyone who knows it’s there.

```
...
from places.views import api
...


urlpatterns = [
    ...
    path("apis/", api.urls),
    ... 
]
```

---

## `import_from_production.py`

This is a reasonably common Django management command pattern that I write. I prefer to use [django-click](https://github.com/GaretJax/django-click) because the [click](https://palletsprojects.com/p/click/) simplifies how to write Python command line interfaces.

We connect to our new endpoint, and if we get a good status code back, we will loop over our results and sync up our database with them.

Please note: I didn’t dive into how to do this security, but you will want to add some protection to your websites unless you are comfortable with it being public.

```
import djclick as click
import requests
from rich import print

from places.models import Place

# Constants
API_URL = "https://your-website.com/apis/places/"


[@click](https://micro.blog/click)()
@click.option("--limit", type=int, default=100)
def command(limit):
    # Start a requests session
    with requests.Session() as session:
        try:
            params = {"limit": limit}
            response = session.get(API_URL, params=params)
            response.raise_for_status()

            items = response.json()["items"]
            for item in items:
                if "name" in item:
                    name = item["name"]
                    address = item["address"]

                    defaults = dict(item)
					# delete foreign keys	
                    del defaults["cuisines"]
                    del defaults["neighborhood"]

                    try:
                        place, created = Place.objects.update_or_create(
                            name=name, address=address, defaults=defaults
                        )
                        print(f"{name} :: {created=}")

                    except Exception as e:
                        print(f"[red]{e=}[/red]")

        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")

        except Exception as err:
            print(f"An error occurred: {err}")
```

## Fin

Overall, I’m pretty happy with this pattern and Django Ninja. My only nitpick is that I wish that Django Ninja shipped with some class-based view batteries. I find them to be much easier to extend and work from than function-based views, but I’m told some third-party apps are starting to help fill in this space.
