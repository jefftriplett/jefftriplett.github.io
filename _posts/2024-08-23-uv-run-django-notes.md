---
category: micro.blog
date: 2024-08-23T12:45:00.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: uv-run-django-notes
title: "📓 UV Run Django Notes"
redirect_to: https://micro.webology.dev/2024/08/23/uv-run-django.html
tags: 
---

I wanted to know how hard it would be to turn one of my [django-startproject](https://github.com/jefftriplett/django-startproject) projects into a `uv run` friendly project. As it turns out, it worked, and the steps were more than reasonable.

Before the PEP 723’ing…
-----------------------

I started with a fairly vanilla `manage.py` that Django will give you after running `python -m manage startproject`.

<div class="highlight">```python
<span style="color:#e6db74">"""Django's command-line utility for administrative tasks."""</span>

<span style="color:#f92672">import</span> os
<span style="color:#f92672">import</span> sys


<span style="color:#66d9ef">def</span> <span style="color:#a6e22e">main</span>():
    <span style="color:#e6db74">"""Run administrative tasks."""</span>
    os<span style="color:#f92672">.</span>environ<span style="color:#f92672">.</span>setdefault(<span style="color:#e6db74">"DJANGO_SETTINGS_MODULE"</span>, <span style="color:#e6db74">"config.settings"</span>)
    <span style="color:#66d9ef">try</span>:
        <span style="color:#f92672">from</span> django.core.management <span style="color:#f92672">import</span> execute_from_command_line
    <span style="color:#66d9ef">except</span> <span style="color:#a6e22e">ImportError</span> <span style="color:#66d9ef">as</span> exc:
        <span style="color:#66d9ef">raise</span> <span style="color:#a6e22e">ImportError</span>(
            <span style="color:#e6db74">"Couldn't import Django. Are you sure it's installed and "</span>
            <span style="color:#e6db74">"available on your PYTHONPATH environment variable? Did you "</span>
            <span style="color:#e6db74">"forget to activate a virtual environment?"</span>
        ) <span style="color:#f92672">from</span> exc
    execute_from_command_line(sys<span style="color:#f92672">.</span>argv)


<span style="color:#66d9ef">if</span> __name__ <span style="color:#f92672">==</span> <span style="color:#e6db74">"__main__"</span>:
    main()

```

</div>shebang
-------

Then we add `#!/usr/bin/env -S uv run` to the top of our `manage.py` file.

Next, we make our `manage.py` executable and try to run it.

<div class="highlight">```shell
$ chmod +x manage.py
$ ./manage.py
ModuleNotFoundError: No module named <span style="color:#e6db74">'django'</span>

```

</div>Our script ran, but Python couldn’t find Django. To tell our script to install Django, we can use `uv add—- script` to add it.

<div class="highlight">```shell
$ uv add --script manage.py django
Updated <span style="color:#e6db74">`</span>manage.py<span style="color:#e6db74">`</span>
$ ./manage.py
...

Type <span style="color:#e6db74">'manage.py help <subcommand>'</span> <span style="color:#66d9ef">for</span> help on a specific subcommand.

Available subcommands:

<span style="color:#f92672">[</span>django<span style="color:#f92672">]</span>
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
Note that only Django core commands are listed as settings are not properly configured <span style="color:#f92672">(</span>error: No module named <span style="color:#e6db74">'environs'</span><span style="color:#f92672">)</span>.

```

</div>Django worked as expected this time, but Python could not find a few third-party libraries I like to include in my projects.

To add these, I passed the other four to `uv add --script` which will add them to the project.

<div class="highlight">```shell
$ uv add --script manage.py django-click <span style="color:#e6db74">"environs[django]"</span> psycopg2-binary whitenoise
Updated <span style="color:#e6db74">`</span>manage.py<span style="color:#e6db74">`</span>
...
$ ./manage.py
...

```

</div>Our Django app’s `manage.py` works when we run it.

After the PEP 723’ing…
----------------------

After we installed our dependencies in our `manage.py` file, they were added to the top of the file between the `///` blocks.

<div class="highlight">```python
<span style="color:#75715e">#!/usr/bin/env -S uv run</span>
<span style="color:#75715e"># /// script</span>
<span style="color:#75715e"># requires-python = ">=3.10"</span>
<span style="color:#75715e"># dependencies = [</span>
<span style="color:#75715e">#     "django",</span>
<span style="color:#75715e">#     "django-click",</span>
<span style="color:#75715e">#     "environs[django]",</span>
<span style="color:#75715e">#     "psycopg2-binary",</span>
<span style="color:#75715e">#     "whitenoise",</span>
<span style="color:#75715e"># ]</span>
<span style="color:#75715e"># ///</span>
<span style="color:#e6db74">"""Django's command-line utility for administrative tasks."""</span>

<span style="color:#f92672">import</span> os
<span style="color:#f92672">import</span> sys


<span style="color:#66d9ef">def</span> <span style="color:#a6e22e">main</span>():
    <span style="color:#e6db74">"""Run administrative tasks."""</span>
    os<span style="color:#f92672">.</span>environ<span style="color:#f92672">.</span>setdefault(<span style="color:#e6db74">"DJANGO_SETTINGS_MODULE"</span>, <span style="color:#e6db74">"config.settings"</span>)
    <span style="color:#66d9ef">try</span>:
        <span style="color:#f92672">from</span> django.core.management <span style="color:#f92672">import</span> execute_from_command_line
    <span style="color:#66d9ef">except</span> <span style="color:#a6e22e">ImportError</span> <span style="color:#66d9ef">as</span> exc:
        <span style="color:#66d9ef">raise</span> <span style="color:#a6e22e">ImportError</span>(
            <span style="color:#e6db74">"Couldn't import Django. Are you sure it's installed and "</span>
            <span style="color:#e6db74">"available on your PYTHONPATH environment variable? Did you "</span>
            <span style="color:#e6db74">"forget to activate a virtual environment?"</span>
        ) <span style="color:#f92672">from</span> exc
    execute_from_command_line(sys<span style="color:#f92672">.</span>argv)


<span style="color:#66d9ef">if</span> __name__ <span style="color:#f92672">==</span> <span style="color:#e6db74">"__main__"</span>:
    main()

```

</div>

Originally posted on: https://micro.webology.dev/2024/08/23/uv-run-django.html