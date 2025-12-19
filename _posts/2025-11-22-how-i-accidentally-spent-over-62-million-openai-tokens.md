---
category: micro.blog
date: 2025-11-23T05:01:54.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: how-i-accidentally-spent-over-62-million-openai-tokens
title: "🤖 How I Accidentally Spent Over 62 Million OpenAI Tokens"
redirect_to: https://micro.webology.dev/2025/11/22/how-i-accidentally-spent-over/
tags:
---

I’ve been fighting a runaway [OpenAI](https://openai.com) bill for the last few weeks. I was worried I was leaking one of my API keys in a non-obvious way, possibly in one of my public projects.

Two weeks ago, I deleted all my keys and contacted OpenAI support. I created new keys for every project, making it easier to track usage and identify any leaks. I had already been doing this, but I was a bit lax on a few projects while migrating from [Digital Ocean](https://www.digitalocean.com) to [Hetzner](https://www.hetzner.com). More on that migration soon.

Fast forward two weeks, and OpenAI notified me again that I hit my very low recharge threshold. With granular keys in place, it only took a minute to narrow down the culprit: my [DjangoTV.com](https://djangotv.com) project.

I use the [OpenAI API](https://platform.openai.com/docs/api-reference/introduction) to help parse presenter names and clean up titles whenever we add new videos. I had recently added [DjangoCon US](https://djangotv.com/videos/djangocon-us/2025/) videos and [Wagtail Space](https://djangotv.com/videos/wagtail-space/2025/) videos during the last two weeks, both on the same day our LLM usage spiked.

I checked my [Django-Q2](https://github.com/django-q2/django-q2) logs and noticed several tasks failing because they were timing out after 90 seconds. The task accepts a list of video IDs and loops through them, parsing each one using [Pydantic AI](https://ai.pydantic.dev) and the OpenAI API. When I ran it from the command line, I never hit a timeout. But when I created a Django Admin Action to bulk process videos, I was trying to process them all in one call instead of fanning them out into individual tasks.

What Went Wrong?
----------------

I didn’t have just one bug - I had two, possibly three bugs that weren’t obvious at the time:

1. **Timeout issues**: Tasks were timing out after 90 seconds when processing large batches
2. **Bulk processing**: Processing all videos in one call instead of individual async tasks
3. **Infinite retries**: I failed to set a maximum number of retry attempts. I assumed that not having a default meant there was a fixed number of retries, not infinite

That third bug was the killer. My job ran for over 24 hours, burning through over 32 million tokens in the process. In total, I spent over 62 million tokens in November before I found and fixed the issue. Thankfully, my out-of-pocket costs were more than reasonable.

What Changed?
-------------

I could blame this on vibecoding since DjangoTV is &gt;99% vibe coded, but the project was built using sensible defaults and this wasn’t obvious at the time.

Here’s what I changed:

- Set `max_attempts` to limit retries
- Kept my 90 second `timeout`
- Spaced out `retry` attempts to a few minutes between tries
- Adjusted my `parse_presenters_with_ai` and `parse_titles_with_ai` Django Admin Actions to queue up one `async_task` per Video instead of processing them all in one call

Sometimes the most expensive bugs are the ones that combine multiple small issues into one perfect storm. Granular API keys for tracking, sensible retry limits, and proper task queuing are now non-negotiable in my projects.

Computers!

---

Written by Jeff. Edited with [Grammarly](https://grammarly.com) and [Claude Code](https://claude.ai/code).

Originally posted on: https://micro.webology.dev/2025/11/22/how-i-accidentally-spent-over/
