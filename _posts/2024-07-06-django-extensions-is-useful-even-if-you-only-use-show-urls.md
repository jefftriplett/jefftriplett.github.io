---
category: micro.blog
date: 2024-07-06T14:00:00.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: django-extensions-is-useful-even-if-you-only-use-show-urls
title: "Django Extensions is useful even if you only use show_urls"
redirect_to: https://micro.webology.dev/2024/07/06/django-extensions-is.html
tags: 
---

Yes, [Django Extensions](https://github.com/django-extensions/django-extensions) package is worth installing, especially for its show\_urls command, which can be very useful for debugging and understanding your project’s URL configurations.

Here’s a short example of how to use it because I sometimes want to include a link to the Django Admin in a menu for staff users, and I am trying to remember what name I need to reference to link to it.

First, you will need to install it via:

<div class="highlight">```bash
pip install django-extensions

<span style="color:#75715e"># or if you prefer using uv like me:</span>
uv pip install django-extensions

```

</div>Next, you’ll want to add `django_extensions` to your `INSTALLED_APPS` in your `settings.py` file:

<div class="highlight">```python
INSTALLED_APPS <span style="color:#f92672">=</span> [
    <span style="color:#f92672">...</span>
    <span style="color:#e6db74">"django_extensions"</span>,
]

```

</div>Finally, to urn the `show_urls` management command you may do some by running your `manage.py` script and passing it the following option:

<div class="highlight">```shell
$ python -m manage show_urls

```

</div>Which will give this output:

<div class="highlight">```shell
$ python -m manage show_urls | grep admin
...
/admin/	django.contrib.admin.sites.index	admin:index
/admin/<app_label>/	django.contrib.admin.sites.app_index	admin:app_list
/admin/<url>	django.contrib.admin.sites.catch_all_view
<span style="color:#75715e"># and a whole lot more...</span>

```

</div>In this case, I was looking for `admin:index` which I can now add to my HTML document this menu link/snippet:

<div class="highlight">```html
... 
<<span style="color:#f92672">a</span> <span style="color:#a6e22e">href</span><span style="color:#f92672">=</span><span style="color:#e6db74">"{% url 'admin:index' %}"</span>>Django Admin</<span style="color:#f92672">a</span>>
... 

```

</div>What I like about this approach is that I can now hide or rotate the url pattern I’m using to get to my admin website, and yet Django will always link to the correct one.

Originally posted on: https://micro.webology.dev/2024/07/06/django-extensions-is.html