---
category: micro.blog
date: '2024-02-29T19:31:04.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: python-s-uv-tool-is-actually-pretty-good
title: Python's UV tool is actually pretty good
redirect_to: https://micro.webology.dev/2024/02/29/pythons-uv-tool-is-actually/
tags:
- Python
- UV
---

I carved out some time recently to start playing with the new Python package installer and resolver, [`uv`](https://github.com/astral-sh/uv).

`uv` makes big promises and claims to be 10-100x faster than pip and pip-tools. From my experiments over the last few weeks, it lives up to this promise.

I’m using it locally for my virtual environments, in my Dockerfiles to rebuild my containers, and for CI using GitHub Actions. Across the board, anything I do with `pip` or `pip-tools` is remarkably faster.

My average GitHub Actions CI workflows dropped from ~2 minutes to 50 seconds. This cuts the minutes I use in half and, in theory, my monthly bill in half.

My goal in sharing my configs is more “show” than “tell' because I will copy and paste these for weeks and months to come.

## local development

Every one of my projects has a `justfile` (it’s like Make but works the same everywhere) with “bootstrap” and “lock” recipes. My “bootstrap” recipe installs everything I need to work with the project locally. I use my “lock” recipe to lock my requirements.txt file so that I’m using the exact requirements locally and in production.

### `justfile` before

My `justfile` might look like this:

```
@bootstrap
    python -m pip install --upgrade pip
    python -m pip install --upgrade --requirement requirements.in
    
@lock *ARGS:
    python -m piptools compile {{ ARGS }} ./requirements.in \
        --resolver=backtracking \
        --output-file ./requirements.txt
```

### `justfile` after

For the most part, `uv` shares most of the same syntax as `pip` so you can start by changing your `pip` references to `uv pip`:

```
@bootstrap
    python -m pip install --upgrade pip uv
    python -m uv pip install --upgrade --requirement requirements.in
    
@lock *ARGS:
    python -m uv pip compile {{ ARGS }} ./requirements.in \
        --resolver=backtracking \
        --output-file ./requirements.txt
```

## Dockerfiles

Everyone’s container setup is going to be different, but I use [Docker](https://www.docker.com) and [Orbstack](https://orbstack.dev), which use a Dockerfile.

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

ENV PATH /venv/bin:$PATH. # this is new
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /srv
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN pip install --upgrade pip uv  # this is updated

RUN python -m uv venv /venv  # this is new

COPY requirements.txt /src/requirements.txt

RUN uv pip install --requirement /src/requirements.txt  # this is updated

WORKDIR /src/
```

## GitHub Actions

GitHub Actions are a little harder to explain, but my workflows started off similar to this before I made the switch to `uv`:

### `main.yml` before

```
  - name: Set up Python 3.12
    uses: actions/setup-python@v5
    with:
      python-version: '3.12'

  - name: Install dependencies
    run: |
            python -m pip install --requirement requirements.in

  - name: Collect Static Assets
    run: |
            python -m manage collectstatic --noinput
```

### `main.yml` after

The biggest pain point that I ran into along the way was related to GitHub Issue [#1386](https://github.com/astral-sh/uv/issues/1386), which has a useable workaround.

```
  - name: Set up Python 3.12
    uses: actions/setup-python@v5
    with:
      python-version: '3.12'

  - name: Install dependencies
    run: |
      python -m pip install uv
      python -m uv venv .venv
      echo "VIRTUAL_ENV=.venv" >> $GITHUB_ENV
      echo "$PWD/.venv/bin" >> $GITHUB_PATH
      python -m uv pip install --requirement requirements.in      

  - name: Collect Static Assets
    run: |
      . .venv/bin/activate
      python -m manage collectstatic --noinput
```

## Conclusion

I hope this was helpful to anyone who is considering making the switch to `uv`. I love to hear about how much time it saves you.

## Updates

2024-03-08 - I modified the ENV PATH statement to prepend instead of replacing the value.
