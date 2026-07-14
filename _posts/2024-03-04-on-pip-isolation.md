---
category: micro.blog
date: '2024-03-04T14:50:39.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: on-pip-isolation
title: On pip isolation
redirect_to: https://micro.webology.dev/2024/03/04/on-pip-isolation/
tags:
- Python
- Today I Learned
---

I saw this [post](https://mastodon.social/@treyhunner/112032637878747686) by [Trey Hunner](https://mastodon.social/@treyhunner) about pip isolation, and I wanted to share a third method.

> I’ve just updated my ~/.config/pip/pip.conf & my dotfiles repo to disallow pip installing outside virtual environments! 🎉
>
> TIL 2 things about #Python’s pip:
>
> 1. pip has a config file. If I ever knew this, I’d forgotten.
> 2. pip has an option that stops it from working outside of a virtual environment!
>
> <https://mastodon.social/@treyhunner/112032637878747686>

To Trey’s point, I never pip to install to easily install anything globally. If I want something installed globally, I can jump through a few hoops to avoid polluting my global pip cache.

My preferred way of disallowing pip installation outside virtual environments is to use the `PIP_REQUIRE_VIRTUALENV` environment variable.

I have `export PIP_REQUIRE_VIRTUALENV=true` set in my `.bash_profile`, which is part of my [`dotfiles`](https://github.com/jefftriplett/dotfiles). I prefer the ENV approach because I share my files over many computers, and it’s one less file to keep up with.

When I want to `pip install` something globally, I use [`pipx`](https://pipx.pypa.io/stable/), which installs each Python application into its isolated environment.

For the few times that I do need to install a Python application globally, I use:

```
PIP_REQUIRE_VIRTUALENV=false python -m pip install \
    --upgrade \
    pip \
    pipx
```

I have this recipe baked into my [global justfile](https://github.com/jefftriplett/dotfiles/blob/f59e2884daace42be404c1f028ea7312fed0bab2/home/justfile#L159-L168) so I can quickly apply upgrades.
