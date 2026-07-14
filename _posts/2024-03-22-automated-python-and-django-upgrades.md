---
category: micro.blog
date: '2024-03-22T16:02:57.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: automated-python-and-django-upgrades
title: Automated Python and Django upgrades
redirect_to: https://micro.webology.dev/2024/03/22/automated-python-and-django-upgrades/
tags:
- Django
- Python
- Today I Learned
---

Recently, I have been maintaining forks for several projects that are no longer maintained. Usually, these are a pain to update, but I have found a workflow that takes the edge off by leveraging [pre-commit](https://github.com/pre-commit/pre-commit).

My process:

* Fork the project on GitHub to whichever organization I work with or my personal account.
* Check out a local copy of my forked copy with git.
* Install [pre-commit](https://github.com/pre-commit/pre-commit)
* Create a `.pre-commit-config.yaml` with *ZERO* formatting or lint changes. This file will only include [django-upgrade](https://github.com/adamchainz/django-upgrade) and [pyupgrade](https://github.com/asottile/pyupgrade) hooks.

We skip the formatters and linters to avoid unnecessary changes if we want to open a pull request in the upstream project. If the project isn’t abandoned, we will want to do that.

* For [django-upgrade](https://github.com/adamchainz/django-upgrade), change the—-target-version option to target the latest version of Django I’m upgrading to, which is currently 5.0.
* For [pyupgrade](https://github.com/asottile/pyupgrade), update the `python` settings under `default_language_version` to the latest version of Python that I’m targetting. Currently, that’s 3.12.

The django-upgrade and pyupgrade projects attempt to run several code formatters and can handle most of the more tedious upgrade steps.

* Run `pre-commit autoupdate` to ensure we have the latest version of our hooks.
* Run `pre-commit run --all-files` to run `pyupgrade` and `django-upgrade` on our project.
* Run any tests contained in the project and review all changes.
* Once I’m comfortable with the changes, I commit them all via git and push them upstream to my branch.

## Example `.pre-commit-config.yaml` config

From my experience, less is more with this bane bones `.pre-commit-config.yaml` config file.

```
# .pre-commit-config.yaml

default_language_version:
  python: python3.12

repos:
  - repo: https://github.com/asottile/pyupgrade
    rev: v3.15.1
    hooks:
      - id: pyupgrade

  - repo: https://github.com/adamchainz/django-upgrade
    rev: 1.16.0
    hooks:
      - id: django-upgrade
        args: [--target-version, "5.0"]
```

If I’m comfortable that the project is abandoned, I’ll add [ruff](https://github.com/astral-sh/ruff) support with a more opinionated config to ease my maintenance burden going forward.
