---
category: micro.blog
date: 2024-06-30T14:00:00.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: using-just-and-compose-for-interactive-django-and-python-debugging-sessions
title: "🐳 Using Just and Compose for interactive Django and Python debugging sessions"
redirect_to: https://micro.webology.dev/2024/06/30/using-just-and.html
tags: 
---

When I wrote REST APIs, I spent weeks and months writing tests and debugging without looking at the front end. It’s all JSON, after all.

For most of my projects, I will open two or three tabs. I’m running Docker Compose in tab one to see the logs as I work. I’ll use the following [casey/just](https://github.com/casey/just) recipe to save some keystrokes and to standardize what running my project looks like:

<div class="highlight">```shell
<span style="color:#75715e"># tab 1</span>
$ just up 

```

</div>In my second tab, I’ll open a shell that is **inside** my main web or app container so that I can interact with the environment, run migrations, and run tests.

We can nitpick the meaning of “console” here, but I tend to have another just recipe for “shell” which will open a Django shell using shell\_plus or something more interactive:

<div class="highlight">```shell
<span style="color:#75715e"># tab 2</span>
$ just console

```

</div>In my third tab, I’ll run a shell session for creating git branches, switching git branches, stashing git changes, and running my linter, which I prefer to run by hand.

<div class="highlight">```shell
<span style="color:#75715e"># tab 3</span>
$ echo <span style="color:#e6db74">"I'm boring"</span>

```

</div>Over the last year or two, the web has returned to doing more frontend work with Django and less with REST. Using `ipdb`, in my view, to figure out what’s going on has been really helpful. Trying to get `ipdb` to “just work” takes a few steps in my normal workflow.

```
# tab 1 (probably)

# start everything
$ just start

# stop our web container
$ just stop web

# start our web container with "--service-ports" 
# just start-web-with-debug

```

The only real magic here is using Docker’s `--service-ports`, which opens ports so we may connect to the open `ipdb` session when we open one in our view code.

My main `justfile` for all of these recipes/workflows looks very similar to this:

<div class="highlight">```yml
<span style="color:#75715e"># justfile</span>
<span style="color:#ae81ff">set dotenv-load := false</span>

<span style="color:#f92672">@build *ARGS</span>:
    <span style="color:#ae81ff">docker compose build {{ ARGS }}</span>

<span style="color:#75715e"># opens a console</span>
<span style="color:#f92672">@console</span>:
    <span style="color:#ae81ff">docker compose run --rm --no-deps utility/bin/bash</span>

<span style="color:#f92672">@down</span>:
    <span style="color:#ae81ff">docker compose down</span>

<span style="color:#f92672">@start *ARGS</span>:
    <span style="color:#ae81ff">just up --detach {{ ARGS }}</span>

<span style="color:#f92672">@start-web-with-debug</span>:
    <span style="color:#ae81ff">docker compose run --service-ports --rm web python -m manage runserver 0.0.0.0:8000</span>

<span style="color:#f92672">@stop *ARGS</span>:
    <span style="color:#ae81ff">docker compose down {{ ARGS }}</span>

<span style="color:#f92672">@up *ARGS</span>:
    <span style="color:#ae81ff">docker compose up {{ ARGS }}</span>

```

</div>If you work on multiple projects, I encourage you to find patterns you can scale across them. Using Just, Make, shell scripts or even Python lightens the cognitive load when switching between them.

Originally posted on: https://micro.webology.dev/2024/06/30/using-just-and.html