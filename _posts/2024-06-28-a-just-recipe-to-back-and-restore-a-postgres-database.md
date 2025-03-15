---
category: micro.blog
date: 2024-06-29T04:58:54.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: a-just-recipe-to-back-and-restore-a-postgres-database
title: "🐘 A Just recipe to back and restore a Postgres database"
redirect_to: https://micro.webology.dev/2024/06/28/a-just-recipe.html
tags:
---

I have used this [casey/just](https://github.com/casey/just) recipe to help backup and restore my Postgres databases from my Docker containers.

I work with a few machines, and it’s an excellent way to create a database dump from one machine and then restore it from another machine. I sometimes use it to test data migrations because restoring a database dump takes a few seconds.

I have been migrating from Docker to [OrbStack](https://orbstack.dev), and the only real pain point is moving data from one volume to another. I sometimes need to switch between the two, so I have recipes set to back up and restore my database from one context to another.

<div class="highlight">```yml
<span style="color:#75715e"># justfile</span>

<span style="color:#ae81ff">set DATABASE_URL := env_var_or_default('DATABASE_URL', 'postgres://postgres@db/postgres')</span>


<span style="color:#75715e"># dump database to file</span>
<span style="color:#f92672">@pg_dump file='db.dump'</span>:
    <span style="color:#ae81ff">docker compose run \</span>
        --<span style="color:#66d9ef">no</span>-<span style="color:#ae81ff">deps \</span>
        --<span style="color:#ae81ff">rm \</span>
        <span style="color:#ae81ff">db \</span>
        <span style="color:#ae81ff">pg_dump \</span>
            --<span style="color:#ae81ff">dbname "{{ DATABASE_URL }}" \</span>
            --<span style="color:#ae81ff">file /code/{{ file }} \</span>
            --<span style="color:#ae81ff">format=c \</span>
            --<span style="color:#ae81ff">verbose</span>

<span style="color:#75715e"># restore database dump from file</span>
<span style="color:#f92672">@pg_restore file='db.dump'</span>:
    <span style="color:#ae81ff">docker compose run \</span>
        --<span style="color:#66d9ef">no</span>-<span style="color:#ae81ff">deps \</span>
        --<span style="color:#ae81ff">rm \</span>
        <span style="color:#ae81ff">db \</span>
        <span style="color:#ae81ff">pg_restore \</span>
            --<span style="color:#ae81ff">clean \</span>
            --<span style="color:#ae81ff">dbname "{{ DATABASE_URL }}" \</span>
            --<span style="color:#ae81ff">if-exists \</span>
            --<span style="color:#66d9ef">no</span>-<span style="color:#ae81ff">owner \</span>
            --<span style="color:#ae81ff">verbose \</span>
            <span style="color:#ae81ff">/code/{{ file }}</span>

```

</div>Shoutout to [Josh Thomas](https://social.joshthomas.dev/@josh) for help on this recipe since we both iterated on this for several projects.

Originally posted on: https://micro.webology.dev/2024/06/28/a-just-recipe.html
