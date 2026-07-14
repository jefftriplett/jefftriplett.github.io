---
category: micro.blog
date: '2024-02-05T05:20:30.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: the-django-apps-i-actually-use-rough-cut
title: The Django apps I actually use (rough cut)
redirect_to: https://micro.webology.dev/2024/02/04/the-django-apps-i-actually/
tags:
- Django
- Python
---

This is an updated version of my response to the [Top 5 3rd party packages](https://forum.djangoproject.com/t/top-5-3rd-party-packages/391) from the Django Forum.

I plan on writing something more in-depth, but life, family, and getting the kids ready for the week got away from me today. Here is my list in case anyone finds them to be helpful.

* `django-allauth`
* `django-click`
* `django-htmx`
* `django-q2`
* `django-test-plus`
* `django-tailwind-cli`
* `django-template-partials`
* `environs[django]`
* `heroicons[django]`
* `neapolitan`
* `python-slugify`
* `ruff` via `pre-commit` but previously was `black`
* `whitenoise`

## Projects I no longer use

* `django-dbbackup` I dropped this app for `DSLR` and then I more recently dropped I dropped them both because I didn’t want to install the extra Postgres files in my containers. I use `pg_backup`, `pg_restore`, and `psql` via the official
