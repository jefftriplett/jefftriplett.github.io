---
category: micro.blog
date: 2024-08-08T03:05:56.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: which-django-and-python-versions-should-i-be-using-today
title: "⬆️ Which Django and Python versions should I be using today?"
redirect_to: https://micro.webology.dev/2024/08/07/which-django-and.html
tags:
---

[Django 5.1 was released](https://www.djangoproject.com/weblog/2024/aug/07/django-51-released/), and I was reminded of the article I wrote earlier this year about [Choosing the Right Python and Django Versions for Your Projects](https://micro.webology.dev/2024/02/01/choosing-the-right.html).

While I encouraged you to wait until the second, third, or even fourth patch release of Django and Python before upgrading, I received a bit of pushback. One interesting perspective claimed that if everyone waits to upgrade, we don’t find critical bugs until the later versions. While that may be plausible, I don’t believe that the dozens of people who read my blog will be swayed by my recommendation to wait for a few patch releases.

I could have emphasized the potential risks of not testing early. Please start testing during the alpha and release candidate phase so that when Django 5.1 is released, your third-party applications will be ready and working on launch day, minimizing the risk of last-minute issues.

Today, I tried to upgrade [Django Packages](https://djangopackages.org) to run on Django 5.1 to see if our test suite would run on Django 5.1, and it very quickly failed in CI due to at least one package not supporting 5.1 yet. Even if it had passed, I’m 90% sure another package would have failed because that’s the nature of running a new major Django or Python release on day one. Even if the third-party package is ready, the packaging ecosystem needs time to catch up.

Which version of Django should I use today?
-------------------------------------------

I’m sticking with **Django 5.0** until Django 5.1’s ecosystem has caught up. I plan to update the third-party packages I help maintain to have Django 5.1 support. After a few patch releases of Django 5.1 have come out and the ecosystem has time to catch up, I will try to migrate again.

Which version of Python should I use today?
-------------------------------------------

I’m starting new projects on **Python 3.12**, with a few legacy projects still being done on Python 3.11. While I am adding Django 5.1 support, I plan to add Python 3.13 support in my testing matrixes to prepare everything for Python 3.13’s release this fall.

Office hours
------------

I plan to spend some of my [Office Hours](https://micro.webology.dev/categories/office-hours/) this week working on Django 5.1 and Python 3.13 readiness for projects I maintain. Please join me if you have a project to update or would like some light-hearted banter to end your week.

Originally posted on: https://micro.webology.dev/2024/08/07/which-django-and.html
