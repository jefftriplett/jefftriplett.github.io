---
category: TIL
date: 2016-03-08
image: https://generator.opengraphimg.com/?atSymbol=true&author=webology&authorSize=text-2xl&style=modern&tags=python%2Cdjango%2Cmixins&title=Django+%60UserPassesTestMixin%60
layout: post
location: Lawrence, Kansas United States
tags:
- python
- django
- mixins
title: Django `UserPassesTestMixin`
---

I stumbled on [`django.contrib.auth.mixins.UserPassesTestMixin`](https://docs.djangoproject.com/en/1.9/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin) while helping a friend out with a quick code review. While the `test_func` feels weird at first, but it's a useful alternative to writing a bunch of one-off decorators.
