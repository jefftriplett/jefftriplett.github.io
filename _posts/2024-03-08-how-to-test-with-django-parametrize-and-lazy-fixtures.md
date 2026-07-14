---
category: micro.blog
date: '2024-03-08T01:53:36.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: how-to-test-with-django-parametrize-and-lazy-fixtures
title: How to test with Django, parametrize, and lazy fixtures
redirect_to: https://micro.webology.dev/2024/03/07/how-to-test-with-django/
tags:
- Django
- Python
---

This article is a follow-up to my post on [How to test with Django and pytest fixtures](https://micro.webology.dev/2024/02/05/how-to-test.html).

Here are some notes on how I prefer to test views for a Django application with authentication using [pytest-lazy-fixture](https://github.com/TvoroG/pytest-lazy-fixture).

## Fixtures

`pytest-django` has a [`django_user_model`](https://pytest-django.readthedocs.io/en/latest/helpers.html#django-user-model) fixture/shortcut, which I recommend using to create valid Django user accounts for your project.

This example assumes that there are four levels of users. We have anonymous (not authenticated), “user,” staff, and superuser levels of permission to work with. Both staff and superusers follow the Django default pattern and have the `is_staff` and `is_superuser` boolean fields set appropriately.

```
# users/tests/fixtures.py
import pytest


@pytest.fixture
def password(db) -> str:
    return "password"


@pytest.fixture
def staff(db, django_user_model, faker, password):
    return django_user_model.objects.create_user(
        email="staff@example.com",
        first_name=faker.first_name(),
        is_staff=True,
        is_superuser=False,
        last_name=faker.last_name(),
        password=password,
    )


@pytest.fixture()
def superuser(db, django_user_model, faker, password):
    return django_user_model.objects.create_user(
        email="superuser@example.com",
        first_name=faker.first_name(),
        is_staff=True,
        is_superuser=True,
        last_name=faker.last_name(),
        password=password,
    )


@pytest.fixture()
def user(db, django_user_model, faker, password):
    return django_user_model.objects.create_user(
        email="user@example.com",
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        password=password,
    )
```

## Testing our views with different User roles

We will assume that our website has some working Category pages that can only viewed by staff or superusers. The `lazy_fixture` library allows us to pass the name of a fixture using parametrize along with the expected status\_code that our view should return.

If you have never seen `parametrize`, it is a nice pytest convention that will re-run the same test multiple times while passing a list of parameters into the test to be evaluated.

The `tp` function variable is a [django-test-plus](https://github.com/revsys/django-test-plus) fixture.

`user`, `staff`, and `superuser` are fixtures we created above.

```
# categories/tests/test_views.py
import pytest

from pytest import param
from pytest_lazyfixture import lazy_fixture


def test_category_noauth(db, tp):
    """
    GET 'admin/categories/'
    """
    url = tp.reverse("admin:category-list")

    # Does this view work with auth?
    response = tp.get(url)
    tp.response_401(response)


@pytest.mark.parametrize(
    "testing_user,status_code",
    [
        param(lazy_fixture("user"), 403),
        param(lazy_fixture("staff"), 200),
        param(lazy_fixture("superuser"), 200),
    ],
)
def test_category_with_auth(db, tp, testing_user, password, status_code):
    """
    GET 'admin/categories/'
    """
    url = tp.reverse("admin:category-list")

    # Does this view work with auth?
    tp.client.login(username=testing_user.email, password=password)
    response = tp.get(url)
    assert response.status_code == status_code
```

## Notes

**Please note:** These status codes are more typical for a REST API. So I would adjust any 40x status codes accordingly.

My goal in sharing these examples is to show that you can get some helpful testing in with a little bit of code, even if the goal isn’t to dive deep and cover everything.

## Updates

To make my example more consistent, I updated `@pytest.mark.django_db()` to use a `db` fixture. Thank you, [Ben Lopatin](https://mastodon.social/@bennylope@social.benlopatin.com/112060829098386312), for the feedback.
