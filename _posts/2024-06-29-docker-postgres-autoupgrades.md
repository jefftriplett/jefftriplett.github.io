---
category: micro.blog
date: 2024-06-30T04:54:41.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: docker-postgres-autoupgrades
title: "🐘 Docker Postgres Autoupgrades"
redirect_to: https://micro.webology.dev/2024/06/29/docker-postgres-autoupgrades.html
tags: 
---

Upgrading Postgres in Docker environments can be daunting, but keeping your database up-to-date is essential for performance, security, and access to new features. While there are numerous guides on manually upgrading Postgres, the process can often be complex and error-prone. Fortunately, the [pgautoupgrade](https://hub.docker.com/r/pgautoupgrade/pgautoupgrade) Docker image simplifies this process, automating the upgrade dance for us.

The Challenge of Upgrading Postgres
-----------------------------------

For many developers, upgrading Postgres involves several manual steps: backing up data, migrating schemas, ensuring compatibility, and testing thoroughly. Mistakes during these steps can lead to downtime or data loss, making the upgrade process a nerve-wracking experience.

The `pgautoupgrade` Docker image is designed to handle the upgrade process seamlessly. Using it in place of the base Postgres image allows you to automate the upgrade steps, reducing the risk of errors and saving valuable time.

How to Use pgautoupgrade
------------------------

While you can use the `pgautoupgrade` directly with Docker, I prefer it as my default development image.

I set my `compose.yml` config with `pgautoupgrade` similar to this config:

<div class="highlight">```yml
<span style="color:#75715e"># compose.yml</span>
<span style="color:#f92672">services</span>:
  <span style="color:#f92672">db</span>:
    <span style="color:#f92672">image</span>: <span style="color:#e6db74">"pgautoupgrade/pgautoupgrade:latest"</span>
    <span style="color:#f92672">volumes</span>:
      - <span style="color:#ae81ff">postgres_data:/var/lib/postgresql/data/</span>
<span style="color:#75715e"># ...</span>

```

</div>Instead of using the latest version of Postgres, `pgautoupgrade` can be set to a specific version. This is nice if you want to match whichever version of Postgres you use in production or if you have extensions that might not be ready to move.

<div class="highlight">```yml
<span style="color:#75715e"># compose.yml</span>
<span style="color:#f92672">services</span>:
  <span style="color:#f92672">db</span>:
    <span style="color:#f92672">image</span>: <span style="color:#e6db74">"pgautoupgrade/pgautoupgrade:16-alpine"</span>
    <span style="color:#f92672">volumes</span>:
      - <span style="color:#ae81ff">postgres_data:/var/lib/postgresql/data/</span>
<span style="color:#75715e"># ...</span>

```

</div>Overall, I’m happy with `pgautoupgrade`. Please note that using `pgautoupgrade` does not mean you should not make data backups.

See my last article, [🐘 A Just recipe to back and restore a Postgres database](https://micro.webology.dev/2024/06/28/a-just-recipe.html) to learn some tips on how to automate using `pg_dump` and `pg_restore`.

Originally posted on: https://micro.webology.dev/2024/06/29/docker-postgres-autoupgrades.html