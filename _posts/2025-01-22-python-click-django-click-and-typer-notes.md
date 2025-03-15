---
category: micro.blog
date: 2025-01-23T00:37:45.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: python-click-django-click-and-typer-notes
title: "Python Click, django-click, and Typer notes"
redirect_to: https://micro.webology.dev/2025/01/22/python-click-djangoclick-and-typer/
tags:
---

One of the most significant Python innovations in my development toolchain was the [Click](https://click.palletsprojects.com) utility, which simplified the creation of Python scripts. Click changed how I approach writing one-off Python scripts and made it easier for me to write better developer experiences around those scripts.

Once I found [django-click](https://github.com/GaretJax/django-click), writing Django management commands was a breeze, using the same Click API that I was already familiar with.

Arguably, the second most significant innovation was the [Typer](https://typer.tiangolo.com) library, built on Click, making writing Python scripts even easier. I didn’t think it was possible to be easier than Python Click until Typer came out and proved me wrong.

The Python Click library
------------------------

A typical pattern I use with Click is creating a command that accepts an argument like a URL.

<div class="highlight">```python
<span style="color:#f92672">import</span> click


[<span style="color:#a6e22e">@click</span>](https:<span style="color:#f92672">//</span>micro<span style="color:#f92672">.</span>blog<span style="color:#f92672">/</span>click)()
<span style="color:#a6e22e">@click</span><span style="color:#f92672">.</span>argument(<span style="color:#e6db74">"url"</span>, type<span style="color:#f92672">=</span>str)
<span style="color:#66d9ef">def</span> <span style="color:#a6e22e">command</span>(url):
	do_something(url<span style="color:#f92672">=</span>url)

```

</div>The Python django-click library
-------------------------------

This works well, but one improvement would be to accept as many `url` arguments as I can pass to it. Thankfully, Click solves this with the `nargs` argument. I always have to look this up, which is why we are here.

<div class="highlight">```python
<span style="color:#f92672">import</span> djclick <span style="color:#66d9ef">as</span> click


[<span style="color:#a6e22e">@click</span>](https:<span style="color:#f92672">//</span>micro<span style="color:#f92672">.</span>blog<span style="color:#f92672">/</span>click)()
<span style="color:#a6e22e">@click</span><span style="color:#f92672">.</span>argument(<span style="color:#e6db74">"urls"</span>, nargs<span style="color:#f92672">=-</span><span style="color:#ae81ff">1</span>, type<span style="color:#f92672">=</span>str)
<span style="color:#66d9ef">def</span> <span style="color:#a6e22e">command</span>(urls):
    <span style="color:#66d9ef">for</span> url <span style="color:#f92672">in</span> urls:
        do_something(url<span style="color:#f92672">=</span>url)

```

</div>The Python Typer library
------------------------

Suppose we were writing this example with Typer. In that case, we could simplify it to using Python’s native data types, which would make it feel more like I’m writing native code and less like I’m using a library.

<div class="highlight">```python
<span style="color:#f92672">import</span> typer


app <span style="color:#f92672">=</span> typer<span style="color:#f92672">.</span>Typer()


[<span style="color:#a6e22e">@app</span>](https:<span style="color:#f92672">//</span>micro<span style="color:#f92672">.</span>blog<span style="color:#f92672">/</span>app)()
<span style="color:#66d9ef">def</span> <span style="color:#a6e22e">command</span>(urls: list[str]):
    <span style="color:#66d9ef">for</span> url <span style="color:#f92672">in</span> urls:
        do_something(url<span style="color:#f92672">=</span>url)

```

</div>Conclusion
----------

There is also a [django-typer](https://github.com/django-commons/django-typer) library, bringing the Typer library to Django. I suspect I’ll switch to django-typer the next time I start a new project to give it a good test drive. I can speculate on what that looks like, but I’ll leave that for another day.

Originally posted on: https://micro.webology.dev/2025/01/22/python-click-djangoclick-and-typer/
