---
category: micro.blog
date: 2024-06-26T03:10:38.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: managing-docker-compose-profiles-with-just-switching-between-default-and-celery-configurations
title: "🐳 Managing Docker Compose Profiles with Just: Switching Between Default and Celery Configurations"
redirect_to: https://micro.webology.dev/2024/06/25/managing-docker-compose.html
tags:
---

For a recent client project, we wanted to toggle between various Docker Compose profiles to run the project with or without Celery.

Using Compose’s `profiles` option, we can label services that we may not want to start by default a label. This might look something like this:

<div class="highlight">```yaml
<span style="color:#f92672">services</span>:

  <span style="color:#f92672">beat</span>:
    <span style="color:#f92672">profiles</span>:
      - <span style="color:#ae81ff">celery</span>
    <span style="color:#ae81ff">...</span>

  <span style="color:#f92672">celery</span>:
    <span style="color:#f92672">profiles</span>:
      - <span style="color:#ae81ff">celery</span>
    <span style="color:#ae81ff">...</span>


  <span style="color:#f92672">web</span>:
    <span style="color:#ae81ff">...</span>

```

</div>We use a [casey/just](https://github.com/casey/just) justfile for some of our common workflows, and I realized I could set a `COMPOSE_PROFILES` environment variable to switch between running a “default” profile and a “celery” profile.

Using just’s [`env_var_or_default`](https://github.com/casey/just?tab=readme-ov-file#environment-variables) feature, we can set both an ENV variable and a default value to fall back on for our project.

<div class="highlight">```bash
<span style="color:#75715e"># justfie </span>

export COMPOSE_PROFILES :<span style="color:#f92672">=</span> env_var_or_default<span style="color:#f92672">(</span><span style="color:#e6db74">'COMPOSE_PROFILES'</span>, <span style="color:#e6db74">'default'</span><span style="color:#f92672">)</span>

@up *ARGS:
    docker compose up <span style="color:#f92672">{{</span> ARGS <span style="color:#f92672">}}</span>

<span style="color:#75715e"># ... the rest of your justfile...</span>


```

</div>To start our service *without Celery*, I would run:

<div class="highlight">```bash
$ just up

```

</div>` To start our service *with Celery*, I would run:

<div class="highlight">```bash
$ export COMPOSE_PROFILES<span style="color:#f92672">=</span>celery
$ just up

```

</div>Our `COMPOSE_PROFILES` environment variable will get passed into our `just up` recipe, and if we don’t include one, it will have a default value of `default`, which will skip running the Celery service.

Originally posted on: https://micro.webology.dev/2024/06/25/managing-docker-compose.html
