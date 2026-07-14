---
category: micro.blog
date: '2024-02-09T02:05:01.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: semi-automate-copy-to-clipboard-case-study
title: Semi-Automate Copy-to-Clipboard Case Study
redirect_to: https://micro.webology.dev/2024/02/08/200501/
tags:
- Django
---

A “copy-to-clipboard” automation is a web page with many formatted text and links that are easy to copy and paste into another application.

My list of links will come from a database, CSV file, JSON file, frontmatter, or a third-party API, depending on what kind of project I am building out.
Once I have my list of links, my automation builds a nicely formatted message based on my link and a text template.

## Django News

For [Django News](https://django-news.com) and [Django News Jobs](https://jobs.django-news.com), I built a few copy-to-clipboard pages to automate writing our weekly tweets for social media and grabbing jobs for our newsletter.

Each newsletter has a title, issue, and description stored in our database, and I use a template like this snippet to build out our weekly announcements.

```
{% raw %}
🎉 The Django News Newsletter {{ object.issue }}

{{ object.issue.description }}

[django-news.com/issues/](https://django-news.com/issues/){{ object.issue.number }}#start
{% endraw %}
```

The result, once published on Mastodon, looks like this: [mastodon.social/@djangone…](https://mastodon.social/@djangonews/111822690418364462)

## Copy-to-Clipboard v2

For my copy-to-clipboard v2, I added [clipboard.js](https://clipboardjs.com/), a JavaScript library that can copy text with the click of a button instead of having to select text and then manually copy the text.

I recently added the [elastic-textarea](https://github.com/cloudfour/elastic-textarea) web component, which resized the text box to fit the text and improved the visual appearance of the text areas.

## DjangoCon US

For DjangoCon US, we have a half dozen copy-to-clipboard pages, which build messages to announce talks on [social media](https://2023.djangocon.us/speaking/twitter/) and build out the metadata we use in our [YouTube videos](https://www.youtube.com/playlist?list=PL2NFhrDSOxgX41jqYSi0HmO9Wsf6WDSmf).
