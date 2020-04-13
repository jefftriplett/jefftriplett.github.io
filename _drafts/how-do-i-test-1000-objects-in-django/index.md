---
category: Django
date: 2020-04-13 10:00 -0500
layout: "post"
slug: "how-do-i-test-1000-objects-in-django"
title: "How do I generate 1,000 objects in Django and DRF to test?"
tags: 
    - django
    - django-restframework
    - drf
    - model-bakery
    - python
---

I get asked questions like quite a bit, so I am going to start blogging about the more common questions. 

## Question

> I am using Django Rest Framework and I need to test an endpoint with at least 1,000 objects.  But putting that in a cycle doesn't seem very optimal to me.
> 
> Do you know of any way to create objects in bulk within the tests?

## Answer

My go-to library of choice for creating test data or more commonly called fixtures in Django tests is [`Model Bakery`](https://github.com/model-bakers/model_bakery). 

With Model Bakery, you pass it a Django model, and it will return a fully baked version of the object for you to test with. Here is an example, based on their [docs](https://model-bakery.readthedocs.io/en/latest/basic_usage.html#basic-usage)

<!-- embedme src/example-01.py -->
```python 
from model_bakery import baker

category = baker.make("news.Category")
```

To create 1,000 categories to test with, we pass the optional `_quantity` parameter to to our `baker.make` method. Here is another example based on the docs [docs](https://model-bakery.readthedocs.io/en/latest/basic_usage.html#more-than-one-instance):

<!-- embedme src/example-02.py -->
```python 
from model_bakery import baker

categories = baker.make("news.Category", _quantity=1000)

assert len(categories) == 1000
```

----

## Bonus Answers

### Bonus Answer 1: It works well with `pytest.fixtures`

If you are using [`pytest`](https://github.com/pytest-dev/pytest) and [`pytest-django`](https://github.com/pytest-dev/pytest-django), one pattern that I use all the time is to create a series of text fixtures for each of my models that I will be testing with.

#### `tests/fixtures.py`

<!-- embedme src/example-03-fixtures.py -->
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

Pytest Fixtures are nice way to reduce the amount of boilerplate code you need for creating and testing objects. To use one of your new tests fixtures, you passed them in as a method argument and pytest will pass the fixture into the test function.

#### `tests/test_models.py`

<!-- embedme src/example-04-test_models.py -->
```python
def test_category(category):
    assert category.name == "Category Name"


def test_post(post):
    assert post.title == "Post Title"
```

For more information about pytest.fixtures, check out the [pytest fixtures: explicit, modular, scalable](https://docs.pytest.org/en/latest/fixture.html) docs.




----

### Bonus Answer 2: It works well for generating non-models 

Model Bakery also has a `prepare` method which is nice for creating valid data for a Django model without saving it to our database. I use this method a lot for testing Django Forms and DRF POST methods. 

<!-- embedme src/example-05.py -->
```python
from model_bakery import baker

from news.serializers import CategorySerializer


def test_category_post(tp):
    # Create a Category fixture
    obj = baker.prepare("news.Category")

    # Use a DRF ModelSerializer to give us JSON
    payload = serializers.CategorySerializer(obj).data

    # Use a reverse lookup to find our endpoint's url
    url = tp.reverse("category-detail")

    # Login as a valid test user
    tp.client.login()

    # Send our test payload to our endpoint
    response = tp.client.post(url, payload, content_type="application/json")

    # Was our request valid?
    tp.response_200(response)
```

----

