---
layout: post
title: "TIL: Django `UserPassesTestMixin`"
date: 2016-03-08
category: TIL
tags:
 - python
 - django
 - mixins
---

I stumbled on [`django.contrib.auth.mixins.UserPassesTestMixin`](https://docs.djangoproject.com/en/1.9/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin) while helping a friend out with a quick code review. While the `test_func` feels weird at first, but it's a useful alternative to writing a bunch of one-off decorators.
