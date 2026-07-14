---
category: micro.blog
date: '2024-02-06T04:57:33.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: how-to-test-with-django-and-pytest-fixtures
title: How to test with Django and pytest fixtures
redirect_to: https://micro.webology.dev/2024/02/05/how-to-test-with-django/
tags:
- Django
- Python
---

Here are some notes on how I like to write tests for a Django app that tests a model down to a view.

## Django Model + pytest Fixture

This part is a mouthful, but I prefer to use the [Model Bakery](https://github.com/model-bakers/model_bakery) library to automatically create instances of Django models (aka a fixture) with good test data instead of manually creating them. This approach saves time and adds some variety to my test data.

We will also use the pytest fixture function to create and return an instance of a Django model using our Model Bakery fixture. This pytest fixture can be used in multiple test cases, ensuring consistency and reducing boilerplate code.

Every app in my project contains a `fixtures.py` file. My news app has a `Category` and a `Post` model, and my fixture looks like this.

```
# news/tests/fixtures.py

import pytest
from model_bakery import baker

@pytest.fixture()
def category(db):
    return baker.make("news.Category", name="Category Name")

@pytest.fixture()
def post(db, category):
    return baker.make("news.Post", title="Post Title", category=category)
```

Please note that a `post` fixture can accept `category` fixture as an argument.

## Configuration

At the top of my project, we will have a `conftest.py` file. This is where we tell pytest to look for our fixtures so they may be automatically loaded.

```
# conftest.py
pytest_plugins = ["news.tests.fixtures"]
```

## Testing our models

Next, we write a very basic test to ensure our fixture can create an instance of a model.

```
# news/tests/test_models.py

def test_get_category(category):
    assert category.name == "Category Name"


def test_get_post(post):
    assert post.title == "Post Title"
```

## Testing our views

I prefer working with [`django-test-plus`](https://github.com/revsys/django-test-plus) because it helps make writing tests cleaner and more straightforward. Then, for every view we have, we will write a test to ensure that our URL patterns match our expected routes and that we return a predicted status code.

```
# news/tests/test_views.py
import pytest

# test that our view resolves to the right uri path
def test_post_uri(tp):
    expected_url = "/"
    reversed_url = tp.reverse("post-list")
    assert expected_url == reversed_url

# test that our view works
def test_post_get(db, tp):
	response = tp.get("post-list")
    tp.assert_http_200_ok(response)
```

## Running tests

To run our tests, we can run pytest.

```
pytest
```
