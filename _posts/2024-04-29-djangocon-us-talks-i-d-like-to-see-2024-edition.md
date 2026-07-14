---
category: micro.blog
date: '2024-04-29T00:45:13.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: djangocon-us-talks-i-d-like-to-see-2024-edition
title: 💚 DjangoCon US Talks I'd Like to See 2024 Edition
redirect_to: https://micro.webology.dev/2024/04/28/djangocon-us-talks-id-like/
tags:
- Django
- Python
- Today I Learned
---

Continuing in my tradition of [2023](https://jefftriplett.com/2023/djangocon-us-talks-i-d-like-to-see-2023-edition/), [2022](https://jefftriplett.com/2022/djangocon-us-talks-i-d-like-to-see-2022-edition/), [2018](https://jefftriplett.com/2018/djangocon-us-talks-i-d-like-to-see-2018-edition/), [2017](https://jefftriplett.com/2017/django-talks-id-like-to-see/), and [2016](https://jefftriplett.com/2016/djangocon-us-talks-id-like-to-see/) “DjangoCon US Talks I’d like to see” annual posts, here is my update for 2024.

This year’s *updated* talk and tutorial deadline is [April 29, 2024, at 12 PM EDT](https://time.is/1200PM_29_Apr_2024_in_New_York?DjangoCon_US_2024_CFP_closes), but check the official [speaking page](https://2024.djangocon.us/speaking/) for updates and [submit your proposal.](https://pretalx.com/djangocon-us-2024/cfp)

Before you read mine, I suggest you check out [Kati Michel’s](https://katherinemichel.github.io/portfolio/djangocon-us-2024-topics-inspiration-list.html) and [Drew Winstel’s](https://winstel.dev/2024/03/01/talk-ideas-for-dcus-24/) list of talk ideas too.

## Modern Django

Three or four years ago, our Django stack was optimized to leverage the Django ORM to tie together a mix of authentication and REST API using the Django REST Framework. The front end was entirely buried by JavaScript, which printed HTML into your browser, and the HTML was entirely hidden away. What used to take a developer hours and days now took weeks because there were so many layers and abstractions to wade through.

Then it all started to change a few years ago, and we learned that we don’t need the additional weeks of development time to use JS/JSON layers for which we may never build that iOS/Android app. We don’t need React for contact us forms, and 90% of our web tasks could be built in a day.

The theme I’d like to see more of this year is doing more with HTML instead of hiding it behind layers of JavaScript.

I want to see lots of talks about technologies like HTMx and frameworks like Tailwind CSS, which are firmly centered inside HTML, instead of trying to avoid using HTML.

## The two non-Python languages we are starting to talk about

Rust and WASM are starting to change everything. How do they fit in with Django and Python?

## Theme: Rust

The Rust language is shaping the landscape of Python productivity in ways that none of us could have predicted. Tools written in Rust are significantly faster and are gaining steam.

* What can a Django developer take from Rust?
* How do I develop a package for Django and Python that uses Rust?
* How libraries like PyDantic are speeding up development (Django Ninja uses it)

## Always nice to have talks

* What’s new in Django 5.x?
* What’s new in Python 3.13?
* What’s new in Wagtail CMS and Django CMS?
* Where do we want the DSF to go?
* How to contribute to Django or third party projects

## Embracing HTML and lightweight front-end frameworks

Last year, I predicted it would be the year of “you probably don’t need JavaScript,” and I still feel good about that. We saw [HTMx](https://htmx.org) take off, but I think Django is still underserved and could benefit from more talks:

* Django 5 added more granular template/form styling , and we could use a talk that deep dives
* Using Django forms with htmx
* Using search with htmx
* Whatever cool things you are doing that I didn’t mention here

## Panel ideas

* Django Fellows panel
* Django content creators' panel
* Django apps and community - It would be nice to hear from the more significant apps and community projects.

## Wagtail CMS

* How do I migrate from WordPress to Wagtail CMS?
* How to properly test with Wagtail CMS for me, because I struggle with it

## Talks I don’t want to see

I find myself at a weird crossroads because I have never discouraged certain topics, but we need to talk more openly about what is bad for our industry and the world instead of avoiding it. Otherwise, we are left with dead air, and people assume we are all on the same page.

To kick us off, there are talks and topics that I do not want to see:

* BAD AI talks and ones that spread more FUD into the community
* crypto talks
* why technology sucks
* proposing a talk because you dislike or even hate something
* bashing other communities
* bashing our communities
* lightning talks disguised as questions (not so much a talk idea, but this has been on my mind for a while)

So please, **none** of these:

* The future of Django depends on AI
* Why tech needs AI
* Crypto talks
* Your product unless you are sponsoring.

## Good luck

You have less than a day, but between my list, [Kati’s list](https://katherinemichel.github.io/portfolio/djangocon-us-2024-topics-inspiration-list.html), and [Drew’s list](https://winstel.dev/2024/03/01/talk-ideas-for-dcus-24/) you have no excuses for saying you didn’t know what to talk about at DjangoCon US this year.

Good luck!
