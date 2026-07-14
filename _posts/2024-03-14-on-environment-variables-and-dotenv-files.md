---
category: micro.blog
date: '2024-03-14T02:23:26.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: on-environment-variables-and-dotenv-files
title: On environment variables and dotenv files
redirect_to: https://micro.webology.dev/2024/03/13/on-environment-variables-and-dotenv/
tags:
- Django
- Python
- Today I Learned
---

Brett Cannon recently vented some frustrations about `.env` files.

> I still hate .env files and their lack of a standard
>
> <https://mastodon.social/@brettcannon@fosstodon.org/112056455108582204>

Brett’s thread and our conversation reminded me that my rule for working with dotenv files is to have my environment load them instead of my Python app trying to read from the `.env` file directly.

## What is a `.env` (dotenv) file?

A `.env` (aka dotenv) is a file that contains a list of key-value pairs in the format of `{key}=value`.

At a basic level, this is what a bare minimum `.env` file might look for in a Django project.

```
# .env
DEBUG=true
SECRET_KEY=you need to change this
```

My go-to library for reading ENV variables is [`environs`](https://github.com/sloria/environs). While the `environs` library can read directly from a dotenv file, don’t do that. I never want my program to read from a file in production because I don’t want a physical file with all of my API keys and secrets.

Most hosting providers, like [Fly.io](https://fly.io), have a command line interface for setting these key-value pairs in production to avoid needing a physical dotenv file.

Instead, we should default to assuming that the ENV variables will bet in our environment, and we should fall back to either a reasonable default value or fail loudly.

Using the `environs` library, my Django `settings.py` file tends to look like this:

```
# settings.py
import environs

env = environs.Env()

# this will default to False if not set.
DEBUG = env.bool("DJANGO_DEBUG", default=False)

# this will error loudly if not set
SECRET_KEY = env.str("SECRET_KEY")

# everything else...
```

I lean on Docker Compose for local development when I’m building web apps because I might have three to five services running. Compose can read a dotenv file and register them into environment variables.

## `.envrc` files aren’t `.env` files

On my macOS, when I’m not developing in a container, I use the [`direnv`](https://direnv.net) application to read an `.envrc` file which is very similar to a dotenv file.

A `.envrc` is very similar to a `.env` file, but to register the values into memory, you have to use Bash’s `export` convention. If you don’t specify `export`, the environment variables won’t be available in your existing Bash environment.

```
# .envrc
export DEBUG=true
export SECRET_KEY=you need to change this
```

I’m a fan of `direnv` because the utility ensures that my environment variables are only set while I am in the same folder or sub-folders that contain the `.envrc` file. If I move to a different folder location or project, `direnv` will automatically unload every environment variable that was previously set.

This has saved me numerous times over the years when I have run a command that might upload a file to s3 and ensure that I’m not uploading to the wrong account because an environment variable is still set from another project.

Clients are generally understanding, but overriding static media for one client with another client’s files is not a conversation I want to have with any client.

`direnv` is excellent insurance against forgetting to unset an environment variable.

## Seeding a `.env` file

I prefer to ship an example `.env.example` file in my projects with reasonable defaults and instructions for copying them over.

```
# .env.example
DEBUG=true
SECRET_KEY=you need to change this
```

If you are a [`casey/just`](https://github.com/casey/just) `justfile` user, I like to ship a `just bootstrap` recipe that checks if a `.env` file already exists. If the `.env` file does not exist, it will copy the example in place.

My `bootstrap` recipe typically looks like this:

```
# justfile
bootstrap *ARGS:
    #!/usr/bin/env bash
    set -euo pipefail

    if [ ! -f ".env" ]; then
        echo ".env created"
        cp .env.example .env
    fi
```

## How do we keep dotenv files in sync?

One pain point when working with dotenv files is keeping new environment variables updated when a new variable has been added.

Thankfully, [modenv](https://github.com/kurtbuilds/modenv) is an excellent utility that can do precisely this. I run `modenv check` and will compare the `.env*` files in the existing folder. It will tell us which files are missing an environment variable when it exists in one but not one of the other files.

I use `modenv check -f` to sync up any missing keys with a blank value. This works well to sync up any new environment variables added to our `.env.example` file with our local `.env` file.

## Alternatives

I recently wrote about [Using Chamber with Django and managing environment variables](https://micro.webology.dev/2024/02/21/using-chamber-with.html), which dives into using Chamber, another tool for managing environment variables.

If you are working with a team, the [1Password CLI](https://developer.1password.com/docs/cli/secrets-environment-variables/)’s `op run` command is an excellent way to share environment variables securely. The tool is straightforward and can be integrated securely with local workflows and CI with just a few steps.
