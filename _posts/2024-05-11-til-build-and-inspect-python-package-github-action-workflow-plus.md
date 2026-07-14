---
category: micro.blog
date: '2024-05-11T01:59:21.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: til-build-and-inspect-python-package-github-action-workflow-plus
title: 🐍 TIL build-and-inspect-python-package GitHub Action workflow plus some bonus Nox + Tox
redirect_to: https://micro.webology.dev/2024/05/10/195921/
tags:
- Python
- Today I Learned
---

TIL: via [@joshthomas](https://mastodon.social/@josh@joshthomas.dev/112419234883043196) via [@treyhunner](https://mastodon.social/@treyhunner/112419178337248517) via [@hynek](https://mastodon.social/@hynek/112418278282018728) about the [hynek/build-and-inspect-python-package](https://github.com/hynek/build-and-inspect-python-package) GitHub Action.

This workflow makes it possible for GitHub Actions to read your Python version classifiers to build a matrix or, as Trey put it, “[Remove so much junk](https://github.com/treyhunner/countdown-cli/pull/208/commits/d33716b471a028ee1c56e35672e94e896dc5f360)” which is a pretty good example.

As a bonus, check out Hynek’s video on [NOX vs TOX – WHAT are they for & HOW do you CHOOSE? 🐍](https://www.youtube.com/watch?v=ImBvrDvK-1U)

<https://www.youtube.com/watch?v=ImBvrDvK-1U>

Both [Nox](https://nox.thea.codes) and [Tox](https://tox.wiki) are great tools that automate testing in multiple Python environments.

I prefer Nox because it uses Python to write configs, which fits my brain better. I used Tox for over a decade, and there are some tox.ini files that I dread updating because I can only remember how I got here after a few hours of tinkering. That’s not Tox’s fault. I think that’s just a limitation of `ini` files and the frustration that comes from being unable to use Python when you have a complex matrix to try and sort out.

I recommend trying them out and using the best tool for your brain. There is no wrong path here.

PS: Thank you, Josh, for bringing this to my attention.
