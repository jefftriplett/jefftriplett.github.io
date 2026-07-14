---
category: micro.blog
date: '2024-03-14T16:51:21.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: python-s-uv-tool-is-even-better
title: Python's UV tool is even better
redirect_to: https://micro.webology.dev/2024/03/14/pythons-uv-tool-is-even/
tags:
- Django
- Python
- UV
---

Last month, I wrote [Python’s UV tool is actually pretty good](https://micro.webology.dev/2024/02/29/pythons-uv-tool.html) about Astral’s new Python package installer and resolver [`uv`](https://github.com/astral-sh/uv), and this is a follow-up post.

Since last month, I have added `uv` to over a dozen projects, and I recently learned that you could skip the `venv` step for projects that use containers or CI where the environment is already isolated.

I mistakenly thought `uv` required a virtual environment (aka venv), but [Josh Thomas](https://joshthomas.dev) recently pointed out that it’s unnecessary.

The trick is to pass the `--system` option, and `uv` will perform a system-wide install. Here’s an example:

```
uv pip install --system --requirement requirement.txt
```

Now that I have seen this, I wish `pip` also used this approach to avoid developers accidentally installing third-party packages globally.

## local development

Nothing has changed with my `justfile` example from last month.

When I’m working with containers, I create a virtual environment (venv) because I will need most of my project requirements installed *outside* of the container so that my text editor and LSP can resolve dependencies. `uv`’s default behavior of respecting a `venv` is all we need here.

Every one of my projects has a `justfile` (it’s like Make but works the same everywhere) with “bootstrap” and “lock” recipes. My “bootstrap” recipe installs everything I need to work with the project locally. I use my “lock” recipe to lock my `requirements.txt` file to use the exact requirements locally and in production.

### `justfile` before

My `justfile` might look like this:

```
@bootstrap
    python -m pip install --upgrade pip
    python -m pip install --upgrade --requirement requirements.in
    
@lock *ARGS:
    python -m piptools compile {{ ARGS }} ./requirements.in \
        --resolver=backtracking \
        --output-file requirements.txt
```

### `justfile` after

For the most part, `uv` shares most of the same syntax as `pip` so you can start by changing your `pip` references to `uv pip`:

```
@bootstrap
    python -m pip install --upgrade pip uv
    python -m uv pip install --upgrade --requirement requirements.in
    
@lock *ARGS:
    python -m uv pip compile {{ ARGS }} requirements.in \
        --resolver=backtracking \
        --output-file requirements.txt
```

## Dockerfiles

Everyone’s container setup is going to be different, but I use [Docker](https://www.docker.com) and [Orbstack](https://orbstack.dev), which use a `Dockerfile`.

## `Dockerfile` before

```
FROM python:3.12-slim-bookworm

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /srv
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN pip install --upgrade pip

COPY requirements.txt /src/requirements.txt

RUN pip install --requirement /src/requirements.txt

WORKDIR /src/
```

## `Dockerfile` after

```
FROM python:3.12-slim-bookworm

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /srv
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN pip install --upgrade pip uv  # this is updated

COPY requirements.txt /src/requirements.txt

RUN uv pip install --system --requirement /src/requirements.txt  # this is updated

WORKDIR /src/
```

## GitHub Actions

GitHub Actions are a little more complicated to explain, but my workflows started similar to this before I made the switch to `uv`:

### `main.yml` before

```
  - name: Set up Python 3.12
    uses: actions/setup-python@v5
    with:
      python-version: '3.12'

  - name: Install dependencies
    run: |
            python -m pip install --requirement requirements.in
```

### `main.yml` after

The most significant pain point I ran into was related to GitHub Issue [#1386](https://github.com/astral-sh/uv/issues/1386), which has a useable workaround.

```
  - name: Set up Python 3.12
    uses: actions/setup-python@v5
    with:
      python-version: '3.12'

  - name: Install dependencies
    run: |
      python -m pip install --upgrade uv  # this is new
      python -m uv pip install --system --requirement requirements.in  # this is updated
```

## Gotchas

The only gotchas I have encountered with `uv` is when I’m trying to install a Python package from a remote zip file.

Previously, I could copy and paste the GitHub repo URL, but `uv` required we use the format `package-name @ url-to-zip-file`

### `requirements.in` before

```
# requirements.in
https://github.com/jefftriplett/django-feedreader/archive/main.zip
```

### `requirements.in` after

```
# requirements.in
django-feedreader @ https://github.com/jefftriplett/django-feedreader/archive/main.zip
```

## Conclusion

This update helps remove a few steps from updating your projects, and it should shave a few minutes off of updating projects to use it.

I hope this was helpful to anyone who is considering making the switch to `uv`. I love to hear about how much time it saves you.
