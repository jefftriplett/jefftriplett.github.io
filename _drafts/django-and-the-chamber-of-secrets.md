---
category: Personal
layout: post
location: Home @ Lawrence, Kansas United States
slug: django-and-the-chamber-of-secrets
title: Django and the Chamber of Secrets
---

## Abstract

Recently I went on a quest to find a better, more secure way to manage my dotenv (.env) files.
For my side projects, I run one monolithic server that primarily runs Docker.
Shipping a new project consists of rsyncing both a docker-compose.yml file along with a dotenv (.env) file and running `docker-compose up -d`.

I run [Watchtower][watchtower] in Docker which looks for new docker images, pulls them, and restart any updated containers automatically.

Overall, I was happy with the setup except for keeping sensitive environment varibles in dotenv files on disk.
After asking some colleagues and friends, someone pointed out [Chamber][chamber] which they were also trying out.
Turns out, Chamber was the best tool for the job.

Since creating this setup, I have shared several gists with curios friends, and this post is meant to be more of an overview of options than it is to be a comprehensive guide to using Chamber. Enjoy!

## Prerequisites

You'll need an AWS account. You'll want some basic Docker and Docker Compose knowledge. You'll want to follow the [Chamber's Installing][chamber-installing] instructions.

## Setting up my environment

Ironically, in my goal to eliminate individual needing to use environment variables, lead me to needing some environment variables. Environment variables I'm using:

- `AWS_ACCESS_KEY_ID`
- `AWS_REGION=us-east-1`
- `AWS_SECRET_ACCESS_KEY`
- `CHAMBER_KMS_KEY_ALIAS=aws/ssm`

## Dockerfile Setup

To make running Chamber running easier, I used the `segment/chamber` Docker image and I copy the `/bin/chamber` binary into my image and I configure it to run it as an `ENTRYPOINT`.

```Dockerfile
FROM segment/chamber:2.8.2 AS chamber

FROM python:3.7-slim-buster AS dev

FROM dev AS production
...
COPY --from=chamber /chamber /bin/chamber
ENTRYPOINT ["/bin/chamber", "exec", "CHANGE-ME-PLZ/production", "--"]
```

Obviously, `CHANGE-ME-PLZ` should be changed based on your project.
Mine are typically a namespace which a combination of my project and the environment like `django-news.com/production`.

By setting the entrypoint inside my Docker image, it makes calling the image in production a bit easier by my not having to think about passing in the entrypoint or me having to manage the environment.

## Docker Compose Setup

```yaml
version: "3.3"
services:
  web:
    entrypoint: /bin/chamber exec CHANGE-ME-PLZ/production --
    command: gunicorn config.wsgi --bind 0.0.0.0:8000
    ...
```

## Using Chamber

Now that you have seen how we use Chamber in Docker and Docker Compose, this is how we get things into Chamber.

### Listing all our projects/

```shell
chamber list-services
```

```shell
chamber list django-news.com/production
```

### Write a new setting

```shell
chamber write django-news.com/production DJANGO_DEBUG true
```

### Delete an existing setting

```shell
chamber delete django-news.com/production DJANGO_DEBUG
```

### Export our settings into a dotenv (.env) file

```shell
chamber export --format=dotenv django-news.com/production
```

## Conclusion

Overall, I'm happy to be able to manage my environment variables from the command line without having to rsync files around.
Using Chamber with KMS increased my monthly AWS bill by $0.01 which is money well spent for the flexability of using Chamber.


## Resources

- https://hub.docker.com/r/segment/chamber
- https://search.gocenter.io/github.com/segmentio/chamber?tab=readme
- https://github.com/Igor-Pchelko/aws-parameter-store-sample/tree/master/scripts
- https://github.com/la-mar/permian-frac-exchange/blob/90ad4720e849678ba987e771be31548944dbab8e/Dockerfile.chamber
- https://docs.aws.amazon.com/kms/latest/developerguide/kms-alias.html
- https://aws.amazon.com/blogs/opensource/demystifying-entrypoint-cmd-docker/

[chamber-docker]: https://hub.docker.com/r/segment/chamber
[chamber-installing]: https://github.com/segmentio/chamber#installing
[chamber]: https://github.com/segmentio/chamber
[watchtower]: https://github.com/containrrr/watchtower