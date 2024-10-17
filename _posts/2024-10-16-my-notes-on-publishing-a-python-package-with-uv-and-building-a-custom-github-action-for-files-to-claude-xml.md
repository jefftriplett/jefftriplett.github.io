---
category: micro.blog
date: 2024-10-17T04:07:08.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: my-notes-on-publishing-a-python-package-with-uv-and-building-a-custom-github-action-for-files-to-claude-xml
title: "📓 My notes on publishing a Python package with UV and building a custom GitHub Action for files-to-claude-xml"
redirect_to: https://micro.webology.dev/2024/10/16/my-notes-on.html
tags: 
---

My new Python application [files-to-claude-xml](https://pypi.org/project/files-to-claude-xml/) is now on PyPI, which means they are packaged and pip installable. My preferred way of running `files-to-claude-xml` is via UV’s tool run, which will install it if it still needs to be installed and then execute it.

<div class="highlight">```shell
$ uv tool run files-to-claude-xml --version

```

</div>Publishing on PyPi with UV
--------------------------

UV has both build and publish commands, so I took them for a spin today.

`uv build` just worked, and a Python package was built.

When I tried `uv publish`, it prompted me for some auth settings for which I had to log in to [PyPI](https://pypi.org) to create a token.

I added those to my local ENV variables I manage with [direnv](https://direnv.net).

<div class="highlight">```shell
export UV_PUBLISH_PASSWORD<span style="color:#f92672">=</span><your-PyPI-token-here>
export UV_PUBLISH_USERNAME<span style="color:#f92672">=</span>__token__

```

</div>Once both were set and registered, `uv publish` published my files on PyPI.

GitHub Action
-------------

To make `files-to-claude-xml` easier to run on GitHub, I created a custom action to build a `_claude.xml` from the GitHub repository.

To use this action, I wrote this example workflow, which runs from [files-to-claude-xml-example](https://github.com/jefftriplett/files-to-claude-xml-example)

<div class="highlight">```yaml
<span style="color:#f92672">name</span>: <span style="color:#ae81ff">Convert Files to Claude XML</span>


<span style="color:#f92672">on</span>:
  <span style="color:#ae81ff">push</span>


<span style="color:#f92672">jobs</span>:
  <span style="color:#f92672">convert-to-xml</span>:
    <span style="color:#f92672">runs-on</span>: <span style="color:#ae81ff">ubuntu-latest</span>
    <span style="color:#f92672">steps</span>:
    - <span style="color:#f92672">uses</span>: <span style="color:#ae81ff">actions/checkout@v4</span>
    - <span style="color:#f92672">name</span>: <span style="color:#ae81ff">Convert files to Claude XML</span>
      <span style="color:#f92672">uses</span>: <span style="color:#ae81ff">jefftriplett/files-to-claude-xml-action@main</span>
      <span style="color:#f92672">with</span>:
        <span style="color:#f92672">files</span>: |<span style="color:#e6db74">
</span><span style="color:#e6db74">          README.md
</span><span style="color:#e6db74">          main.py</span>          
        <span style="color:#f92672">output</span>: <span style="color:#e6db74">'_claude.xml'</span>
        <span style="color:#f92672">verbose</span>: <span style="color:#e6db74">'true'</span>
    - <span style="color:#f92672">name</span>: <span style="color:#ae81ff">Upload XML artifact</span>
      <span style="color:#f92672">uses</span>: <span style="color:#ae81ff">actions/upload-artifact@v4</span>
      <span style="color:#f92672">with</span>:
        <span style="color:#f92672">name</span>: <span style="color:#ae81ff">claude-xml</span>
        <span style="color:#f92672">path</span>: <span style="color:#ae81ff">_claude.xml</span>

```

</div>My GitHub action is built with a `Dockerfile`, which installs `files-to-claude-xml`.

<div class="highlight">```Dockerfile
<span style="color:#75715e"># Dockerfile</span><span style="color:#960050;background-color:#1e0010">
</span><span style="color:#960050;background-color:#1e0010"></span><span style="color:#66d9ef">FROM</span><span style="color:#e6db74"> ghcr.io/astral-sh/uv:bookworm-slim</span><span style="color:#960050;background-color:#1e0010">
</span><span style="color:#960050;background-color:#1e0010">
</span><span style="color:#960050;background-color:#1e0010">
</span><span style="color:#960050;background-color:#1e0010"></span><span style="color:#66d9ef">ENV</span> UV_LINK_MODE<span style="color:#f92672">=</span>copy


<span style="color:#66d9ef">RUN</span> --mount<span style="color:#f92672">=</span>type<span style="color:#f92672">=</span>cache,target<span style="color:#f92672">=</span>/root/.cache/uv <span style="color:#ae81ff">\
</span><span style="color:#ae81ff"></span>    --mount<span style="color:#f92672">=</span>type<span style="color:#f92672">=</span>bind,source<span style="color:#f92672">=</span>uv.lock,target<span style="color:#f92672">=</span>uv.lock <span style="color:#ae81ff">\
</span><span style="color:#ae81ff"></span>    --mount<span style="color:#f92672">=</span>type<span style="color:#f92672">=</span>bind,source<span style="color:#f92672">=</span>pyproject.toml,target<span style="color:#f92672">=</span>pyproject.toml <span style="color:#ae81ff">\
</span><span style="color:#ae81ff"></span>    uv sync --frozen --no-install-project<span style="color:#960050;background-color:#1e0010">
</span><span style="color:#960050;background-color:#1e0010">
</span><span style="color:#960050;background-color:#1e0010">
</span><span style="color:#960050;background-color:#1e0010"></span><span style="color:#66d9ef">WORKDIR</span><span style="color:#e6db74"> /app</span><span style="color:#960050;background-color:#1e0010">
</span><span style="color:#960050;background-color:#1e0010">
</span><span style="color:#960050;background-color:#1e0010">
</span><span style="color:#960050;background-color:#1e0010"></span><span style="color:#66d9ef">ENTRYPOINT</span> [<span style="color:#e6db74">"uvx"</span>, <span style="color:#e6db74">"files-to-claude-xml"</span>]<span style="color:#960050;background-color:#1e0010">
</span>
```

</div>To turn a GitHub repository into a runnable GitHub Action, an `action.yml` file needs to exist in the repository. This file describes the input arguments and which `Dockerfile` or command to run.

<div class="highlight">```yml
<span style="color:#75715e"># action.yml</span>
<span style="color:#f92672">name</span>: <span style="color:#e6db74">'Files to Claude XML'</span>
<span style="color:#f92672">description</span>: <span style="color:#e6db74">'Convert files to XML format for Claude'</span>
<span style="color:#f92672">inputs</span>:
  <span style="color:#f92672">files</span>:
    <span style="color:#f92672">description</span>: <span style="color:#e6db74">'Input files to process'</span>
    <span style="color:#f92672">required</span>: <span style="color:#66d9ef">true</span>
    <span style="color:#f92672">type</span>: <span style="color:#ae81ff">list</span>
  <span style="color:#f92672">output</span>:
    <span style="color:#f92672">description</span>: <span style="color:#e6db74">'Output XML file path'</span>
    <span style="color:#f92672">required</span>: <span style="color:#66d9ef">false</span>
    <span style="color:#f92672">default</span>: <span style="color:#e6db74">'_claude.xml'</span>
  <span style="color:#f92672">verbose</span>:
    <span style="color:#f92672">description</span>: <span style="color:#e6db74">'Enable verbose output'</span>
    <span style="color:#f92672">required</span>: <span style="color:#66d9ef">false</span>
    <span style="color:#f92672">default</span>: <span style="color:#e6db74">'false'</span>
  <span style="color:#f92672">version</span>:
    <span style="color:#f92672">description</span>: <span style="color:#e6db74">'Display the version number'</span>
    <span style="color:#f92672">required</span>: <span style="color:#66d9ef">false</span>
    <span style="color:#f92672">default</span>: <span style="color:#e6db74">'false'</span>
<span style="color:#f92672">runs</span>:
  <span style="color:#f92672">using</span>: <span style="color:#e6db74">'docker'</span>
  <span style="color:#f92672">image</span>: <span style="color:#e6db74">'Dockerfile'</span>
  <span style="color:#f92672">args</span>:
    - <span style="color:#ae81ff">${{ join(inputs.files, ' ') }}</span>
    - --<span style="color:#ae81ff">output</span>
    - <span style="color:#ae81ff">${{ inputs.output }}</span>
    - <span style="color:#ae81ff">${{ inputs.verbose == 'true' && '--verbose' || '' }}</span>
    - <span style="color:#ae81ff">${{ inputs.version == 'true' && '--version' || '' }}</span>

```

</div>Overall, this works. Claude’s prompting helped me figure it out, which felt fairly satisfying given the goal of `files-to-claude-xml`.

Originally posted on: https://micro.webology.dev/2024/10/16/my-notes-on.html