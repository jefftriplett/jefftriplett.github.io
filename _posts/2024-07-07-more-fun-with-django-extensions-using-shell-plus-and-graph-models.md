---
category: micro.blog
date: 2024-07-07T15:13:45.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: more-fun-with-django-extensions-using-shell-plus-and-graph-models
title: "🧰 More fun with Django Extensions using `shell_plus` and `graph_models`"
redirect_to: https://micro.webology.dev/2024/07/07/more-fun-with.html
tags:
---

[Yesterday](https://micro.webology.dev/2024/07/06/django-extensions-is.html), I wrote about [Django Extensions](https://github.com/django-extensions/django-extensions) `show_urls` management command because it’s useful. I have Mastodon posted/tooted about it \[previously\](<https://mastodon.social/@webology/110271223054909764>, but I didn’t expect it to possibly [lead to it being added to Django](https://github.com/django/django/pull/18347), and yet here we are. My favorite byproduct of blogging is when someone talks about something they like, and someone asks, “What if” or “Why doesn’t?” and then they get inspired to look into it and contribute. This post might have led to one new contribution to Django. 🎉

[Several](https://mastodon.social/@greg@gregnewman.io/112740008247060792) [people](https://mastodon.social/@fallenhitokiri@social.screamingatmyscreen.com/112740068077125373) [shared](https://mastodon.social/@carlton@fosstodon.org/112740235823924270) that they also liked Django Extensions `shell_plus` and `graph_models` management commands.

I don’t use `shell_plus` often, but I bake it into my Just workflows for clients who do. I tend to forget about it, and I spend so much time using `pytest.set_trace()` and testing.

If you haven’t used `graph_models`, I use it in most of my client projects. I generate SVG files with it and add them to an ERD section of their docs, which helps discuss models and onboard new developers. It’s a nice-to-have feature and is a small lift with a huge payoff. This code is also easy to copy and paste from project to project.

Originally posted on: https://micro.webology.dev/2024/07/07/more-fun-with.html
