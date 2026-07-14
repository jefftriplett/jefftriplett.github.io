---
category: micro.blog
date: '2024-02-22T04:01:19.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: using-chamber-with-django-and-managing-environment-variables
title: Using Chamber with Django and managing environment variables
redirect_to: https://micro.webology.dev/2024/02/21/using-chamber-with-django-and/
tags:
- Django
- Python
- Today I Learned
---

One of my favorite hosting setups is getting a cheap slice from Digital Ocean or your favorite provider, installing [Docker Compose](https://docs.docker.com/compose/) and [Tailscale](https://tailscale.com), and then fire-walling everything off except for port 443.

Whenever I want to host a new project, I copy a `docker-compose.yml` file to the server, and then I start it with `docker compose up -d'.

I run [Watchtower](https://github.com/containrrr/watchtower) in Docker on the server, which looks for new Docker images from GitHub Packages, pulls them, and restarts any updated containers.

I can update my projects, `git push` changes, and GitHub Actions will build and store a new container image for me.

My main pain point was juggling environment variables until someone pointed out [Chamber](https://github.com/segmentio/chamber), which manages environment variables well.

Since creating this setup, I have shared several GitHub Gists with curious friends, and my goal of this post is to serve as more of an overview of options than it is to be a comprehensive guide to using Chamber.

## Prerequisites

You’ll need an AWS account, some essential Docker and Compose knowledge, and to follow [Chamber’s Installing](https://github.com/segmentio/chamber#installing) instructions.

## Setting up my environment

Ironically, my goal of eliminating individual environment variables led me to need four environment variables to bootstrap Chamber itself.
The environment variables I’m using:

* `AWS_ACCESS_KEY_ID`
* `AWS_REGION`
* `AWS_SECRET_ACCESS_KEY`
* `CHAMBER_KMS_KEY_ALIAS=aws/ssm`

## Dockerfile Setup

To make running Chamber running more straightforward, I used the `segment/chamber` Docker image, copied the `/bin/chamber` binary into my image, and configured it to run it as a `ENTRYPOINT`.

```
FROM segment/chamber:2.14 AS chamber

FROM python:3.11-slim-buster AS dev

FROM dev AS production
...
COPY --from=chamber /chamber /bin/chamber
ENTRYPOINT ["/bin/chamber", "exec", "django-news.com/production", "--"]
```

I prefer to namespace these variables based on the project and the environment I’m referencing, like `django-news.com/production`.

I am using a Docker entrypoint so that my secrets/environment variables work by default, whether running the image or overriding the default command, so I may shell into my container.

## Docker Compose Setup

```
services:
  web:
    entrypoint: /bin/chamber exec django-news.com/production --
    command: gunicorn config.wsgi --bind 0.0.0.0:8000
    ...
```

Please note that the `entrypoint` line is optional if you set it in your `ENTRYPOINT` setting in your `DOCKERFILE`.

## Using Chamber

Now that you have seen how we use Chamber in Docker and Docker Compose, this is how we get things into Chamber.

### Listing our projects

```
$ chamber list-services
```

```
$ chamber list django-news.com/production
```

### Write new settings

```
$ chamber write django-news.com/production DJANGO_DEBUG true
```

### Delete an existing setting

```
$ chamber delete django-news.com/production DJANGO_DEBUG
```

### Export our settings into a dotenv (.env) file

```
$ chamber export --format=dotenv django-news.com/production
```

### Consuming an env variable from Django

The [`environs`](https://github.com/sloria/environs) project is my go-to for parsing environment variables. Here is an example of how to toggle Django’s debug mode.

```
# settings.py
import environs

env = environs.Env()

DEBUG = env.bool("DJANGO_DEBUG", default=False)
```

## Conclusion

I’m happy to manage my environment variables from the command line without syncing files.
Using Chamber with KMS increased my monthly AWS bill by $0.01, which is money well spent for the flexibility of using Chamber.

## Alternatives

I had a good experience using the 1Password CLI for a recent client project to share and load secrets into the environment.
If you are working with a team, consider checking it out for your team in case it’s a good fit.
Check out their [Load secrets into the environment](https://developer.1password.com/docs/cli/secrets-environment-variables/) docs.
