---
category: Django
date: 2020-04-14 13:52 -0500
image: https://generator.opengraphimg.com/?atSymbol=true&author=webology&authorSize=text-2xl&style=modern&tags=django%2Cdjango-restframework%2Cdrf%2Cmodel-bakery%2Cpython&title=How+do+I+generate+1%2C000+objects+in+Django+and+DRF+to+test%3F
layout: post
location: Home @ Lawrence, Kansas United States
slug: how-do-i-test-1000-objects-in-django
tags:
- django
- django-restframework
- drf
- model-bakery
- python
title: How do I generate 1,000 objects in Django and DRF to test?
weather: 50˚F Clear
---

Earlier this week, [Isa Buriticá](https://twitter.com/iris9112) asked me a great question about how to bulk create and test items in a Django test and I wanted to share that information on my website.

## Question

> I am using Django Rest Framework and I need to test an endpoint with at least 1,000 objects.  But putting that in a cycle doesn't seem very optimal to me.
> 
> Do you know of any way to create objects in bulk within the tests?
>
> [Isa Buriticá](https://twitter.com/iris9112)

## Answer

My go-to library of choice for creating test data, more commonly called “fixtures” in Django tests, is [`Model Bakery`](https://github.com/model-bakers/model_bakery).

With Model Bakery, you can pass in a Django model or model reference, and Bakery will create an object based on that model type.
This fully-baked object includes valid test data so that each required field has the right type of data it needs.

Here is an example, based on their [docs](https://model-bakery.readthedocs.io/en/latest/basic_usage.html#basic-usage):

<!-- [[[cog
import cog
from pathlib import Path

def embedme(filename: str) -> str:
    path = Path(cog.inFile).parent.joinpath(filename)
    content = path.read_text().strip()
    cog.outl(f"```python\n{content}\n```")

embedme("src/example-01.py")
]]] -->
```python
from model_bakery import baker

category = baker.make("news.Category")

assert category.name
```
<!-- [[[end]]] -->

To create 1,000 categories for a  test, we pass the optional `_quantity` parameter to our `baker.make` method.
Here is another example based on the [docs](https://model-bakery.readthedocs.io/en/latest/basic_usage.html#more-than-one-instance):

<!-- [[[cog
embedme("src/example-02.py")
]]] -->
```python
from model_bakery import baker

categories = baker.make("news.Category", _quantity=1000)

assert len(categories) == 1000
```
<!-- [[[end]]] -->

----

## Bonus Answers

### Bonus Answer 1: It works well with `pytest.fixtures`

If you are using [`pytest`](https://github.com/pytest-dev/pytest) and [`pytest-django`](https://github.com/pytest-dev/pytest-django), one pattern that I use all the time is to create a series of text fixtures for each of my models that I will be testing with.

#### `tests/fixtures.py`

<!-- [[[cog
embedme("src/example-03-fixtures.py")
]]] -->
```python
import pytest

from model_bakery import baker


@pytest.fixture()
def category(db):
    return baker.make("news.Category", name="Category Name")


@pytest.fixture()
def post(db, category):
    return baker.make("news.Post", category=category, title="Post Title")
```
<!-- [[[end]]] -->

pytest fixtures are nice way to reduce the amount of boilerplate code you need for creating and testing objects.
To use one of your new tests fixtures, you pass them in as a method argument and pytest will pass the fixture into the test function.

#### `tests/test_models.py`

<!-- [[[cog
embedme("src/example-04-test_models.py")
]]] -->
```python
def test_category(category):
    assert category.name == "Category Name"


def test_post(post):
    assert post.title == "Post Title"
```
<!-- [[[end]]] -->

For more information about pytest.fixtures, check out the [pytest fixtures: explicit, modular, scalable](https://docs.pytest.org/en/latest/fixture.html) docs.

----

### Bonus Answer 2: It works well for generating test data

Model Bakery also has a `prepare` method which is useful for creating valid test data for a Django model without saving it to our database.
I use this method often for testing Django Forms and DRF POST methods.

<!-- [[[cog
embedme("src/example-05.py")
]]] -->
```python
from model_bakery import baker

from news.serializers import CategorySerializer


def test_category_post(tp):
    # Create a Category fixture
    obj = baker.prepare("news.Category")

    # Use a DRF ModelSerializer to give us JSON
    payload = CategorySerializer(obj).data

    # Use a reverse lookup to find our endpoint's url
    url = tp.reverse("category-detail")

    # Login as a valid test user
    tp.client.login()

    # Send our test payload to our endpoint
    response = tp.client.post(url, payload, content_type="application/json")

    # Was our request valid?
    tp.response_200(response)
```
<!-- [[[end]]] -->

----

Thanks to [Will Vincent](https://wsvincent.com/) for advice on and corrections to a draft of this article.
