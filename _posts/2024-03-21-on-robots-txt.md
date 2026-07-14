---
category: micro.blog
date: '2024-03-21T00:36:02.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: on-robots-txt
title: 🤖 On Robots.txt
redirect_to: https://micro.webology.dev/2024/03/20/on-robotstxt/
tags:
- Django
---

I have spent a lot of mental energy thinking about how to be more defensive with the `robots.txt` files in my projects.

> **robots.txt** is the [filename](https://en.wikipedia.org/wiki/Filename "Filename") used for implementing the **Robots Exclusion Protocol**, a standard used by [websites](https://en.wikipedia.org/wiki/Website "Website") to indicate to visiting [web crawlers](https://en.wikipedia.org/wiki/Web_crawler "Web crawler") and other [web robots](https://en.wikipedia.org/wiki/Internet_bot "Internet bot") which portions of the website they are allowed to visit.
>
> <https://en.wikipedia.org/wiki/Robots.txt>

In theory, this file helps control what search engines and AI scrapers are allowed to visit, but I need more confidence in its effectiveness in the post-AI apocalyptic world.

Over the last few weeks, I have added and updated a static `robots.txt` file on several projects. Since then, I have noticed the number of known AI scrapers has doubled, and then some. See [Dark Visitors](https://darkvisitors.com) for a comprehensive list of known AI agents.

Today, I decided to switch to the [`django-robots`](https://github.com/jazzband/django-robots) project because I can update it from the Django admin. Since `django-robot`’s rules are stored in a database, I can automate updating them.

## My research so far

These websites and articles have seemed helpful so far.

* [Block the Bots that Feed “AI” Models by Scraping Your Website](https://neil-clarke.com/block-the-bots-that-feed-ai-models-by-scraping-your-website/)
* [Go ahead and block AI web crawlers](https://coryd.dev/posts/2024/go-ahead-and-block-ai-web-crawlers/)
* [Dark Visitors](https://darkvisitors.com)
* [Your Pika robots.txt File](https://pika.pika.page/posts/your-pika-robots-txt-file)

### Django resources

* [Add robots.txt to a Django website](https://learndjango.com/tutorials/add-robotstxt-django-website)
* [How to add a robots.txt to your Django site](https://adamj.eu/tech/2020/02/10/robots-txt/)
