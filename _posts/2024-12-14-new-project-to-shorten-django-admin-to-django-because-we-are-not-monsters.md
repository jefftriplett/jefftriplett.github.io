---
category: micro.blog
date: 2024-12-15T03:18:43.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: new-project-to-shorten-django-admin-to-django-because-we-are-not-monsters
title: "New project to shorten django-admin to django because we are not monsters"
redirect_to: https://micro.webology.dev/2024/12/14/new-project-to.html
tags:
---

One of the biggest mysteries in Django is why I have to run `django-admin` from my terminal instead of just running `django`. Confusingly, `django-admin` has nothing to do with Django’s admin app.

If you have ever wondered why and wanted to type `django` from your terminal, my new project, `django-cli-no-admin` solves this problem for you.

I looked for several package names on [PyPI](https://pypi.org), including `django-cli`, which I liked the best (someone is name squatting this package.)

I gave up and went with [`django-cli-no-admin`](https://pypi.org/project/django-cli-no-admin/) for lack of a better name.

<div class="highlight">```shell
<span style="color:#75715e"># new school</span>
uv pip install django-cli-no-admin

<span style="color:#75715e"># old school</span>
pip install django-cli-no-admin

<span style="color:#75715e"># to use it...</span>
django --version

```

</div>This tool aliases Django’s `django-admin` script does but we shorted the name by 50%:

<div class="highlight">```toml
[<span style="color:#a6e22e">project</span>.<span style="color:#a6e22e">scripts</span>]
<span style="color:#a6e22e">django</span> = <span style="color:#e6db74">"django.core.management:execute_from_command_line"</span>

```

</div>Should Django adopt this?
-------------------------

Yes. But we can leave `django-admin` alone since we have ~20 years of history referencing it.

How long has this lived in your head?
-------------------------------------

Almost two decades.

Originally posted on: https://micro.webology.dev/2024/12/14/new-project-to.html
