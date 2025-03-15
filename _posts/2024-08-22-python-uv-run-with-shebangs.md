---
category: micro.blog
date: 2024-08-22T18:54:45.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: python-uv-run-with-shebangs
title: "🐍 Python UV run with shebangs"
redirect_to: https://micro.webology.dev/2024/08/22/python-uv-run.html
tags:
---

This [UV shebang](https://simonwillison.net/2024/Aug/21/usrbinenv-uv-run/) trick that Simon Willison linked up is a nice pattern, and I plan to rebuild some of my one-off scripts in my [dotfiles](https://github.com/jefftriplett/dotfiles) using it.

Here is a demo that will print “hello python” using the Python Branding colors using the [Rich](https://github.com/Textualize/rich) library while letting UV install and manage rich for you.

<div class="highlight">```python
<span style="color:#75715e">#!/usr/bin/env -S uv run</span>
<span style="color:#75715e"># /// script</span>
<span style="color:#75715e"># requires-python = ">=3.10"</span>
<span style="color:#75715e"># dependencies = [</span>
<span style="color:#75715e">#     "rich",</span>
<span style="color:#75715e"># ]</span>
<span style="color:#75715e"># ///</span>

<span style="color:#f92672">from</span> rich.console <span style="color:#f92672">import</span> Console
<span style="color:#f92672">from</span> rich.theme <span style="color:#f92672">import</span> Theme

python_theme <span style="color:#f92672">=</span> Theme(
    {
        <span style="color:#e6db74">"pyyellow"</span>: <span style="color:#e6db74">"#ffde57"</span>,
        <span style="color:#e6db74">"pyblue"</span>: <span style="color:#e6db74">"#4584b6"</span>,
    }
)

console <span style="color:#f92672">=</span> Console(theme<span style="color:#f92672">=</span>python_theme)

console<span style="color:#f92672">.</span>print(<span style="color:#e6db74">"[pyyellow]hello[/pyyellow] [pyblue]python[/pyblue]"</span>, style<span style="color:#f92672">=</span><span style="color:#e6db74">"on #646464"</span>)

```

</div>Assuming you have UV installed, and you save and `chmod +x` this file as `hello-python.py`, then you should be able to run it via `hello-python.py.`

I suspect I can more easily bootstrap new machines using this trick without fewer worries about polluting my global system packages.

Originally posted on: https://micro.webology.dev/2024/08/22/python-uv-run.html
