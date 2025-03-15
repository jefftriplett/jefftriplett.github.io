---
category: micro.blog
date: 2024-09-19T19:18:30.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: uv-roundup-five-good-articles-and-a-pre-commit-tip
title: "🤠 UV Roundup: Five good articles and a pre-commit tip"
redirect_to: https://micro.webology.dev/2024/09/19/uv-roundup-five.html
tags:
---

I have written quite a bit about [UV](https://micro.webology.dev/categories/uv/) on my [micro blog](https://micro.webology.dev), and I am happy to see more and more people adopt it. I have stumbled on so many good articles recently that I wanted to share them because every article points out something new or different about why UV works well for them.

If you are new to [UV](https://github.com/astral-sh/uv), it’s a new tool written by [Astral](https://astral.sh/), the creators of [Ruff](https://github.com/astral-sh/ruff).

I like UV because it replaces, combines, or complements a bunch of Python tools into one tool and user developer experience without forcing a UV way of doing it. UV effectively solves the question, “Why do I need another Python tool?” to do everyday Python tasks.

Some reason I like UV after using it for months:

- It’s a faster pip and is really, really fast
- It can install and manage Python versions
- It can run and install Python scripts
- It can run single-file Python scripts along with their dependencies
- It can handle project lock files

While some people don’t care about UV being fast, it’s shaved minutes off my CI builds and container rebuilds, which means it has also saved me money and energy resources.

Overall thoughts on UV
----------------------

Oliver Andrich’s [UV — I am (somewhat) sold](https://andrich.me/2024/09/uv-i-am-somewhat-sold/) takes the approach of only using UV to set up a new Python environment. Oliver uses UV to install Python, aliases to call Python, and UV tool install to set up a few global utilities.

Using UV with Django
--------------------

Anže Pečar’s [UV with Django](https://blog.pecar.me/uv-with-django) shows how to use UV to set up a new project with Django.

Switching from pyenv to UV
--------------------------

Will Guaraldi Kahn-Greene’s [Switching from pyenv to uv](https://bluesock.org/~willkg/blog/dev/switch_pyenv_to_uv.html) was relatable for me because I also use pyenv, but I plan to slowly migrate to using only UV. I’m already halfway there, but I will have pyenv for my legacy projects for years because many aren’t worth porting yet.

Using UV and managing with Ansible
----------------------------------

Adam Johnson’s [Python: my new uv setup for development](https://adamj.eu/tech/2024/09/18/python-uv-development-setup/) taught me to use `uv cache prune` to clean up unused cache entries and shows how he manages his UV setup using Ansible.

Some notes on UV
----------------

Simon Willison’s [Notes on UV](https://simonwillison.net/2024/Sep/15/uv-i-am-somewhat-sold/) is an excellent summary of Oliver’s notes.

A parting UV tip
----------------

If you are a pre-commit fan hoping for a version that supports UV, the [`pre-commit-uv`](https://github.com/tox-dev/pre-commit-uv) project does just that. I started updating my justfile recipes to bake `just lint` to the following `uv run` command, which speeds up running and installing pre-commit significantly.

<div class="highlight">```bash
$ uv run --with pre-commit-uv pre-commit run --all-files
pre-commit-uv

```

</div>If you are attending DjangoCon US…
----------------------------------

If you are attending DjangoCon US and want to talk UV, Django, [Django News](https://django-news.com), [Django Packages](https://djangopackages.org), hit me up while you are there.

I’ll be attending, volunteering, organizing, [sponsoring](https://mastodon.social/@JoshFoxleyTalent@fosstodon.org/113165161818979000), and sprinting around the venue in Durham, NC, for the next week starting this Friday.

We still have [online and in-person tickets](https://ti.to/defna/djangocon-us-2024), but not much longer!

Originally posted on: https://micro.webology.dev/2024/09/19/uv-roundup-five.html
