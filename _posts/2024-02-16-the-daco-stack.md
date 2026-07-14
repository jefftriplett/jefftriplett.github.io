---
category: micro.blog
date: '2024-02-16T02:36:33.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: the-daco-stack
title: The DACO Stack
redirect_to: https://micro.webology.dev/2024/02/15/the-daco-stack/
tags:
- Django
- Python
---

For the last few months, I have used the Django + Adam Johnson + Carlton Gibson + Oliver Andrich stack, or what I’m calling the DACO stack. Maybe the DjACO stack rolls off the tongue more easily.

The DACO stack combines new Django tech with wrappers around libraries like Heroicons, TailwindCSS, and htmx, which integrates a nice modern front-end development experience with Django.

## `carltongibson/neapolitan`

The [Neapolitan](https://github.com/carltongibson/neapolitan) project brings CRUD views to Django in what feels like a marriage between the Django Admin meets Django Rest Framework’s model viewsets but focused on the front-end. Neapolitan gives you CRUD views for your application in a few lines of Python code.

I have used it on several projects where I wanted to quickly build a front end around some data and give a limited number of people access to help maintain it.

## `adamchainz/django-htmx`

Adam’s `django-htmx` adds htmx support to Django.

<https://github.com/adamchainz/django-htmx>

## `carltongibson/django-template-partials`

Carlton’s `django-template-partials` project helps create reusable inline template blocks. When paired with `django-htmx`, we can render a form, search results, and individual table rows without rewriting the web page.

<https://github.com/carltongibson/django-template-partials>

## `adamchainz/heroicons`

Adam brings the [Heroicons](https://heroicons.com) library to Django, a series of SVG images that are nice for navigation menus and anywhere you might want to embed an icon image quickly. Heroicons is one of my goto libraries for quickly adding extra polish for apps that I might normally fall back to boring text links.

<https://github.com/adamchainz/heroicons>

## `oliverandrich/django-tailwind-cli`

Oliver’s `django-tailwind-cli` project integrates Tailwind CSS
into Django, includes a live reload server, and enables `python manage.py tailwind` to work.

<https://github.com/oliverandrich/django-tailwind-cli>

## Conclusion

Try the DACO stack and let me know if it saves you time and if you find some new tools to add to it.
