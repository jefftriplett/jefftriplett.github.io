---
category: micro.blog
date: '2024-03-24T04:26:41.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: on-scratching-itches-with-python
title: On scratching itches with Python
redirect_to: https://micro.webology.dev/2024/03/23/on-scratching-itches-with-python/
tags:
- Django
- Python
---

Python is such a fantastic glue language. Last night, while watching March Madness basketball games, I had a programming itch I wanted to scratch.

I dusted off a demo I wrote several years ago. It used Python’s subprocess module, which strings together a bunch of shell commands to perform a git checkout, run a few commands, and then commit the results. The script worked, but I struggled to get it fully working in a production environment.

To clean things up and as an excuse to try out a new third-party package, I converted the script to use:

* [GitPython](https://github.com/gitpython-developers/GitPython) - GitPython is a Python library used to interact with Git repositories.
* [Shelmet](https://github.com/dgilland/shelmet) - A shell power-up for working with the file system and running subprocess commands.
* [Django Q2](https://github.com/django-q2/django-q2) - A multiprocessing distributed task queue for Django based on Django-Q.

Using Django might have been overkill, but having a Repository model to work with felt nice. Django Q2 was also overkill, but if I put this app into production, I’ll want a task queue, and Django Q2 has a manageable amount of overhead.

GitPython was a nice improvement over calling git commands directly because their API makes it easier to see which files were modified and to check against existing branch names. I was happy with the results after porting my subprocess commands to the GitPython API.

The final package I used is a new package called Shelmet, which was both a nice wrapper around subprocess plus they have a nice API for file system operations in the same vein as Python’s Pathlib module.

## Future goals

I was tempted to cobble together a GitHub bot, but I didn’t need one. I might dabble with the GitHub API more to fork a repo, but for now, this landed in a better place, so when I pick it back up again in a year, I’m starting in a good place.

If you want to write a GitHub bot, check out [Mariatta](https://github.com/Mariatta)’s [black\_out](https://github.com/Mariatta/black_out) project.
