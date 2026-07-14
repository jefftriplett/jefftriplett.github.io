---
category: micro.blog
date: '2024-05-22T22:21:37.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: what-s-new-in-django-5-1
title: ✨ What's new in Django 5.1
redirect_to: https://micro.webology.dev/2024/05/22/whats-new-in-django/
tags:
- Django
---

With today’s [Django 5.1 alpha 1](https://www.djangoproject.com/weblog/2024/may/22/django-51-alpha-1-released/) release, picking just one favorite feature is hard. Django 5.1 is scheduled for release this August.

I highly recommend reading the [release notes](https://docs.djangoproject.com/en/dev/releases/5.1/) on everything included in the next release.

Here are a few of my favorite features that are solid quality-of-life improvements.

## `ModelAdmin.list_display`

> `django.contrib.admin`
>
> `ModelAdmin.list_display` now supports using `__` lookups to list fields from related models.

Many times a year, I forget that `list_display` does not support the dunder `__` lookup, which leads to adding a property on `ModelAdmin` instead. FINALLY, Django supports this and I’m thrilled.

## The `querystring` template tag

> `{% querystring %}` template tag
>
> Django 5.1 introduces the [`{% querystring %}`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#std-templatetag-querystring) template tag, simplifying the modification of query parameters in URLs, making it easier to generate links that maintain existing query parameters while adding or changing specific ones.

This is one of those template tags that I routinely add to my projects because it’s so helpful. I’m thrilled to no longer need it.

## Views require authentication by default

> Middleware to require authentication by default
>
> The new `LoginRequiredMiddleware` redirects all unauthenticated requests to a login page. Views can allow unauthenticated requests by using the new `login\_not\_required() decorator.

Django now ships with a `LoginRequiredMiddleware` middleware, which adds authentication to all pages by default.

I’m happy to see this because >90% of the apps I build require authentication by default, and it’d be easier/less code to mark views that do not need required auth. Plus, it feels more secure to have a way to default all views to using auth than to forget to decorate a view that should not be visible.

I’m not sure how this impacts using third-party apps with views yet, but I suspect there will be a reasonable solution.

## One more thing…

There are dozens and dozens of new features in the [Django 5.1 release notes](https://docs.djangoproject.com/en/dev/releases/5.1/). If you spot any gems or have any favorite features, please let me know.
