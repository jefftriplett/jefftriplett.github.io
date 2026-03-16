---
category: micro.blog
date: 2026-02-27T02:56:51.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: how-i-use-django-simple-nav-for-dashboards-command-palettes-and-more
title: "How I Use django-simple-nav for Dashboards, Command Palettes, and More"
redirect_to: https://micro.webology.dev/2026/02/26/how-i-use-djangosimplenav-for/
tags:
---

I first got exposed to [django-simple-nav](https://github.com/westerveltco/django-simple-nav) while working with [Josh Thomas](https://github.com/joshuadavidthomas) at [the Westervelt Corporation](https://github.com/westerveltco) over the last two or three years. It quickly became a go-to library in my toolkit. django-simple-nav lets you define nav items and groupings in Python, then hand them off to a Django template to render. I use it for sidebars, headers, dashboards, and other spots where I need a menu.

Since then, I have also started using it on a lot of personal projects. It has been a great fit every time.

Defining nav items once and reusing them everywhere
---------------------------------------------------

Recently I wanted to reuse parts of a menu nav without having to update a bunch of different files. I had a dashboard with a sidebar full of links, and I also wanted a command palette that could search across all those same options when you hit Command-K from any page. django-simple-nav was a natural fit because you define your items once in Python and render them with whatever template you want.

Here is an example of what that looks like in Python:

<div class="highlight">```python
<span style="color:#f92672">from</span> django_simple_nav.nav <span style="color:#f92672">import</span> Nav
<span style="color:#f92672">from</span> django_simple_nav.nav <span style="color:#f92672">import</span> NavGroup
<span style="color:#f92672">from</span> django_simple_nav.nav <span style="color:#f92672">import</span> NavItem

NAV_ITEMS <span style="color:#f92672">=</span> [
    NavItem(title<span style="color:#f92672">=</span><span style="color:#e6db74">"Home"</span>, url<span style="color:#f92672">=</span><span style="color:#e6db74">"home"</span>),
    NavItem(title<span style="color:#f92672">=</span><span style="color:#e6db74">"Dashboard"</span>, url<span style="color:#f92672">=</span><span style="color:#e6db74">"dashboard"</span>),
    NavGroup(
        title<span style="color:#f92672">=</span><span style="color:#e6db74">"Admin & Tools"</span>,
        items<span style="color:#f92672">=</span>[
            NavItem(title<span style="color:#f92672">=</span><span style="color:#e6db74">"Admin"</span>, url<span style="color:#f92672">=</span><span style="color:#e6db74">"admin:index"</span>, permissions<span style="color:#f92672">=</span>[<span style="color:#e6db74">"is_staff"</span>]),
        ],
    ),
    NavItem(title<span style="color:#f92672">=</span><span style="color:#e6db74">"Login"</span>, url<span style="color:#f92672">=</span><span style="color:#e6db74">"login"</span>),
    NavItem(title<span style="color:#f92672">=</span><span style="color:#e6db74">"Logout"</span>, url<span style="color:#f92672">=</span><span style="color:#e6db74">"logout"</span>),
]


<span style="color:#66d9ef">class</span> <span style="color:#a6e22e">DashboardNav</span>(Nav):
    template_name <span style="color:#f92672">=</span> <span style="color:#e6db74">"nav/dashboard.html"</span>
    items <span style="color:#f92672">=</span> NAV_ITEMS


<span style="color:#66d9ef">class</span> <span style="color:#a6e22e">CommandPaletteNav</span>(Nav):
    template_name <span style="color:#f92672">=</span> <span style="color:#e6db74">"nav/command_palette.html"</span>
    items <span style="color:#f92672">=</span> NAV_ITEMS


```

</div>Flexible URLs and named routes
------------------------------

A few things to notice here. When you create a nav item and you have a URL, you can either use the URL’s name or you can give it the path to it and it will figure out what it is. So if I want a nav item for the Django admin, I can use `"admin:index"` as the URL.

Handling permissions without template logic
-------------------------------------------

Another nice feature is the `permissions` parameter. The Admin link uses `permissions=["is_staff"]`, which means it only shows up for staff users. You can use this to hide things based on whether someone is staff, a superuser, or has specific Django permissions. This makes it nice to keep all of your nav options in one place without having to write special conditional logic in your templates to show or hide items for different users.

Rendering a dashboard nav with Django templates
-----------------------------------------------

The other thing to notice is the two Nav classes at the bottom: `DashboardNav` and `CommandPaletteNav`. They both use the same `NAV_ITEMS` list but point to different templates. This is where the reuse really shines.

Here is an example nav template at `templates/nav/dashboard.html`:

<div class="highlight">```html
<<span style="color:#f92672">nav</span>>
  {% for item in items %}
    {% if item.items %}
      <<span style="color:#f92672">span</span>>{{ item.title }}:
        {% for subitem in item.items %}
          <<span style="color:#f92672">a</span> <span style="color:#a6e22e">href</span><span style="color:#f92672">=</span><span style="color:#e6db74">"{{ subitem.url }}"</span><span style="color:#960050;background-color:#1e0010">{%</span> <span style="color:#a6e22e">if</span> <span style="color:#a6e22e">subitem</span><span style="color:#960050;background-color:#1e0010">.</span><span style="color:#a6e22e">active</span> <span style="color:#960050;background-color:#1e0010">%}</span> <span style="color:#a6e22e">class</span><span style="color:#f92672">=</span><span style="color:#e6db74">"active"</span><span style="color:#960050;background-color:#1e0010">{%</span> <span style="color:#a6e22e">endif</span> <span style="color:#960050;background-color:#1e0010">%}</span>>
            {{ subitem.title }}
          </<span style="color:#f92672">a</span>>
        {% endfor %}
      </<span style="color:#f92672">span</span>>
    {% else %}
      <<span style="color:#f92672">a</span> <span style="color:#a6e22e">href</span><span style="color:#f92672">=</span><span style="color:#e6db74">"{{ item.url }}"</span><span style="color:#960050;background-color:#1e0010">{%</span> <span style="color:#a6e22e">if</span> <span style="color:#a6e22e">item</span><span style="color:#960050;background-color:#1e0010">.</span><span style="color:#a6e22e">active</span> <span style="color:#960050;background-color:#1e0010">%}</span> <span style="color:#a6e22e">class</span><span style="color:#f92672">=</span><span style="color:#e6db74">"active"</span><span style="color:#960050;background-color:#1e0010">{%</span> <span style="color:#a6e22e">endif</span> <span style="color:#960050;background-color:#1e0010">%}</span>>
        {{ item.title }}
      </<span style="color:#f92672">a</span>>
    {% endif %}
  {% endfor %}
</<span style="color:#f92672">nav</span>>

```

</div>Then in your base template, you can render it with the template tag:

<div class="highlight">```html
{% load django_simple_nav %}

{% django_simple_nav "myapp.nav.DashboardNav" %}

```

</div>Building a command palette from the same nav items
--------------------------------------------------

Because the `CommandPaletteNav` class uses the same `NAV_ITEMS` list but with a different template, we can render the same nav data as JSON for a command palette. Here is an example template at `templates/nav/command_palette.html`:

<div class="highlight">```html
{% load django_simple_nav %}

<<span style="color:#f92672">script</span> <span style="color:#a6e22e">type</span><span style="color:#f92672">=</span><span style="color:#e6db74">"application/json"</span> <span style="color:#a6e22e">id</span><span style="color:#f92672">=</span><span style="color:#e6db74">"command-palette-data"</span>>
[{<span style="color:#f92672">%</span> <span style="color:#66d9ef">for</span> <span style="color:#a6e22e">item</span> <span style="color:#66d9ef">in</span> <span style="color:#a6e22e">items</span> <span style="color:#f92672">%</span>}{<span style="color:#f92672">%</span> <span style="color:#66d9ef">if</span> <span style="color:#a6e22e">item</span>.<span style="color:#a6e22e">items</span> <span style="color:#f92672">%</span>}{<span style="color:#f92672">%</span> <span style="color:#66d9ef">for</span> <span style="color:#a6e22e">subitem</span> <span style="color:#66d9ef">in</span> <span style="color:#a6e22e">item</span>.<span style="color:#a6e22e">items</span> <span style="color:#f92672">%</span>}
  {<span style="color:#e6db74">"title"</span><span style="color:#f92672">:</span> <span style="color:#e6db74">"{{ subitem.title }}"</span>, <span style="color:#e6db74">"url"</span><span style="color:#f92672">:</span> <span style="color:#e6db74">"{{ subitem.url }}"</span>, <span style="color:#e6db74">"group"</span><span style="color:#f92672">:</span> <span style="color:#e6db74">"{{ item.title }}"</span>}{<span style="color:#f92672">%</span> <span style="color:#66d9ef">if</span> <span style="color:#a6e22e">not</span> <span style="color:#a6e22e">forloop</span>.<span style="color:#a6e22e">last</span> <span style="color:#a6e22e">or</span> <span style="color:#a6e22e">not</span> <span style="color:#a6e22e">forloop</span>.<span style="color:#a6e22e">parentloop</span>.<span style="color:#a6e22e">last</span> <span style="color:#f92672">%</span>},{<span style="color:#f92672">%</span> <span style="color:#a6e22e">endif</span> <span style="color:#f92672">%</span>}{<span style="color:#f92672">%</span> <span style="color:#a6e22e">endfor</span> <span style="color:#f92672">%</span>}{<span style="color:#f92672">%</span> <span style="color:#66d9ef">else</span> <span style="color:#f92672">%</span>}
  {<span style="color:#e6db74">"title"</span><span style="color:#f92672">:</span> <span style="color:#e6db74">"{{ item.title }}"</span>, <span style="color:#e6db74">"url"</span><span style="color:#f92672">:</span> <span style="color:#e6db74">"{{ item.url }}"</span>}{<span style="color:#f92672">%</span> <span style="color:#66d9ef">if</span> <span style="color:#a6e22e">not</span> <span style="color:#a6e22e">forloop</span>.<span style="color:#a6e22e">last</span> <span style="color:#f92672">%</span>},{<span style="color:#f92672">%</span> <span style="color:#a6e22e">endif</span> <span style="color:#f92672">%</span>}{<span style="color:#f92672">%</span> <span style="color:#a6e22e">endif</span> <span style="color:#f92672">%</span>}{<span style="color:#f92672">%</span> <span style="color:#a6e22e">endfor</span> <span style="color:#f92672">%</span>}
]
</<span style="color:#f92672">script</span>>

```

</div>This also lent itself well when I was trying to do something quickly with Claude. I don’t know how to build a command palette, but I was able to just have Claude create one. I asked it to use HTMX to keep everything pretty lightweight.

Final thoughts
--------------

All in all, django-simple-nav is a nice library to have in your toolkit. I like using it for headers, menus, dashboard navigation links, and even footer text. If you need flexible, reusable navigation in Django, give it a look.

---

Written by Jeff. Edited with [Grammarly](https://grammarly.com) and [Claude Code](https://claude.ai/code).

Originally posted on: https://micro.webology.dev/2026/02/26/how-i-use-djangosimplenav-for/
