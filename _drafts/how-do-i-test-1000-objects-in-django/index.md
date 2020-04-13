---
category: Django
date: 2020-04-13 10:00 -0500
title: "How do I generate 1,000 objects in Django and DRF to test?"
---

I get asked questions like quite a bit, so I am going to start blogging about the more common questions. 

## Question
{: .pt-4 .text-blue-800}

> I am using Django Rest Framework and I need to test an endpoint with at least 1,000 objects.  But putting that in a cycle doesn't seem very optimal to me.

> Do you know of any way to create objects in bulk within the tests?

## Answer
{: .pt-4 .text-blue-800}

My go-to library of choice for creating test data or more commonly called fixtures in Django tests is [`Model Bakery`](https://github.com/model-bakers/model_bakery). 

With Model Bakery, you pass it a Django model, and it will return a fully baked version of the object for you to test with. Here is an example, based on their [docs](https://model-bakery.readthedocs.io/en/latest/basic_usage.html#basic-usage)

<!-- embedme example-01.py -->
```python 
from model_bakery import baker

category = baker.make("news.Category")
```

So that's great for one instance, but how do you create 1,000 objects to test again? Here is another example modified from their [docs](https://model-bakery.readthedocs.io/en/latest/basic_usage.html#more-than-one-instance)

<!-- embedme example-02.py -->
```python 
from model_bakery import baker

categories = baker.make("news.Category", _quantity=1000)

assert len(categories) == 1000
```

----

## Bonus Answers
{: .pt-4 .text-blue-800}

### Bonus Answer #1 - It works well with `pytest.fixtures`
{: .pt-4 .text-blue-800}

If you are using pytest and pytest-django, one pattern that I use all the time is to create a series of text fixtures for each of my models that I will be testing with.

`# tests/fixtures.py`

<!-- embedme example-03.py -->
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

`# tests/test_models.py`

<!-- embedme example-04.py -->
```python
def test_category(category):
    assert category.name == "Category Name"


def test_post(post):
    assert post.title == "Post Title"

```

### Bonus Answer #2 - It works well for generating non-models 
{: .pt-4 .text-blue-800}
