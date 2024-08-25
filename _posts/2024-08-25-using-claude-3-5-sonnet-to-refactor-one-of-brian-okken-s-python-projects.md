---
category: micro.blog
date: 2024-08-25T19:46:23.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: using-claude-3-5-sonnet-to-refactor-one-of-brian-okken-s-python-projects
title: "🚜 Using Claude 3.5 Sonnet to refactor one of Brian Okken's Python projects"
redirect_to: https://micro.webology.dev/2024/08/25/using-claude-sonnet.html
tags: 
---

Brian Okken [posted](https://mastodon.social/@brianokken@fosstodon.org/113023568032444293) and published his [Top pytest Plugins](https://pythontest.com/top-pytest-plugins/) script and then a follow-up post, [Finding the top pytest plugins](https://pythontest.com/pytest/finding-top-pytest-plugins/), which was pretty cool.

I have written a few throw-away scripts, which William Vincent wrote about and updated a few times in the [Top 10 Django Third-Party Packages (2024)](https://learndjango.com/tutorials/essential-django-3rd-party-packages) and [The 10 Most-Used Django Packages (2024)](https://learndjango.com/tutorials/10-most-used-django-packages).

These efforts are powered by [Hugo von Kemenade](https://github.com/hugovk/)’s excellent [Top PyPI Packages](https://hugovk.github.io/top-pypi-packages/).

This inspired me to fork Brian’s [top-pytest-plugins](https://github.com/okken/top-pytest-plugins) project, which I updated to support passing in other package names like “django” to get a rough estimate of monthly package downloads.

The refactored project is [jefftriplett/top-python-packages](https://github.com/jefftriplett/top-python-packages).

**Please note:** Looking at the package name doesn’t scale as well for projects that have their own [Trove classifiers](https://pypi.org/classifiers/). For a project like pytest, it works well. Many of the top packages may not even have Django in their name for a project like Django. Some projects may even actively discourage a project from using their project in their package’s name for trademark reasons. So, YMMV applies here.

Prompts
-------

I added `uv run` support, which I have [written about a lot lately](https://micro.webology.dev/categories/uv/).

I also copied the `top_pytest.py` file into a Claude 3.5 Sonnet session, and I let it handle the whole refactor. It even handled adding the [PEP 723](https://peps.python.org/pep-0723/) new package dependencies without me asking it to.

In case it’s useful to anyone, here are my prompts:

<div class="highlight">```plaintext
## Prompt:
Please update this script to use a rich table.


## Prompt:
Please update the table styles to be ascii so I can copy and paste it into a markdown doc


## Prompt:
Please remove the description column


## Prompt:
Please change all PyTest and pytest references to Django and django


## Prompt:
Please add back `if 'django' in project.lower() and 'django' != project.lower():`


## Prompt:
please remove the \*# Export to markdown section. I can just pipe the output \*


## Prompt:
Please add the typer library.


## Prompt:
Please remove days and limit


## Prompt:
Please refactor the script to allow me to pass the package name instead of django. You can default to django though.


This way I can pass pytest or flask or other projects.


## Prompt:
Please change the default Table box type to MARKDOWN

```

</div>Outro
-----

I don’t usually write about Claude or prompts, but the tool has been handy lately.

If you have had some similar successes, let me know. I have been exploring some rabbit holes, and it’s changing the way I approach solving problems.

Originally posted on: https://micro.webology.dev/2024/08/25/using-claude-sonnet.html