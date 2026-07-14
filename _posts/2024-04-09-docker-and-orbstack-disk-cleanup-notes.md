---
category: micro.blog
date: '2024-04-09T02:07:22.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: docker-and-orbstack-disk-cleanup-notes
title: 🐳 Docker and OrbStack disk cleanup notes
redirect_to: https://micro.webology.dev/2024/04/08/docker-and-orbstack-disk-cleanup/
tags:
---

[Docker](https://www.docker.com) is one of my daily drivers, and here are my notes for reclaiming disk space and a bonus tip for getting a faster runtime.

---

## Docker “Containers” Prune

Most of the time, when I run into a Docker issue, it’s because I have out of disk space allocated for Docker containers and images.

90% of the time, you can reclaim the most disk space by running `docker system prune`.

**Why?** Docker’s default behavior is to remove “stopped containers,” which are instances of containers that have already run and are no longer valid. There is no good reason to keep these around, so **I consider this a safe operation** to run.

```
$ docker system prune
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all dangling images
  - unused build cache

Are you sure you want to continue? [y/N] y
Deleted Containers:
...
Total reclaimed space: 127.5GB
```

I freed up 127.5 GB of disk space when I ran this today.

---

## Docker “Images” Prune

The `docker system df` will show us how much disk space Docker uses and what storage types.

```
$ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          100       0         64.76GB   64.76GB (100%)
Containers      0         0         0B        0B
Local Volumes   1211      0         32.79GB   32.79GB (100%)
Build Cache     638       0         31.29GB   31.29GB
```

The `docker image prune -a' will delete all images that don’t have a container associated with them.

**Why?** Worse case, if you delete an image that you need, you can always rebuild it. If you are using a third-party image, you can always `docker pull` a more recent image. **I consider this a safe operation** to run.

```
$ docker image prune -a
WARNING! This will remove all images without at least one container associated to them.
Are you sure you want to continue? [y/N] y
...
Total reclaimed space: 11.28GB
```

The results after we have run our command:

```
$ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          0         0         0B        0B
Containers      0         0         0B        0B
Local Volumes   1211      0         32.79GB   32.79GB (100%)
Build Cache     638       0         31.29GB   31.29GB
```

---

## Docker “Build Cache” Prune

Docker’s Build Cache stores or caches all of the various build steps that Docker will use to assemble an image.

**I consider this a safe operation** because the worst-case scenario of a build step not being cached is that it takes a little longer to run your next Docker build while Docker re-runs the command.

```
$ docker builder prune
...
Total:  31.29GB
```

```
$ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          0         0         0B        0B
Containers      0         0         0B        0B
Local Volumes   1211      0         32.79GB   32.79GB (100%)
Build Cache     2         0         0B        0B
```

---

## Docker “Local Volumes” Prune

Docker volumes are where your persistent data lives, like the files your database needs between sessions.

**I do not recommend bulk deleting all of your volumes.**

Unless you really, really mean it, and you know what you are doing, leave `docker volume prune` alone.

I have “Local Volumes” that have lived longer than some Javascript Frameworks have.

Instead, only delete what you know you aren’t using anymore via:

```
$ docker volume ls
$ docker volume rm {volume-name}
```

---

## OrbStack for extra performance

If you are on macOS, try out [OrbStack](https://orbstack.dev), which lives up to its claim of being lightning faster than Docker.

I run both Docker and Orbstack on my machines, and I use a `DOCKER_CONTEXT` environment variable to change between the two contexts.

```
# for OrbStack
export DOCKER_CONTEXT=orbstack
$ docker system df
...

# for Docker
export DOCKER_CONTEXT=default
$ docker system df
...
```

If you aren’t sure what your “context” options are, you can run `docker context ls` to see them:

```
$ docker context ls
NAME              DESCRIPTION                               DOCKER ENDPOINT                                        ERROR
default           Current DOCKER_HOST based configuration   unix:///var/run/docker.sock
desktop-linux *   Docker Desktop                            unix:///Users/username/.docker/run/docker.sock
orbstack          OrbStack                                  unix:///Users/username/.orbstack/run/docker.sock
```
