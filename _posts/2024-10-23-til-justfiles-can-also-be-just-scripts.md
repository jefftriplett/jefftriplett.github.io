---
category: micro.blog
date: 2024-10-23T17:04:47.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: til-justfiles-can-also-be-just-scripts
title: "TIL Justfiles can also be Just Scripts"
redirect_to: https://micro.webology.dev/2024/10/23/til-justfiles-can.html
tags: 
---

TIL that Justfiles can turn into Just Scripts by adding `#!/usr/bin/env just --justfile` to the top of the file and running `chmod +x` on the file.

From the docs:

> By adding a shebang line to the top of a `justfile` and making it executable, `just` can be used as an interpreter for scripts: <https://github.com/casey/just?tab=readme-ov-file#just-scripts>

`just.sh`
---------

<div class="highlight">```shell
<span style="color:#75715e">#!/usr/bin/env just --justfile
</span><span style="color:#75715e"></span>
@_default:
	just --justfile just.sh --list

@lint *ARGS:
    uv --quiet run --with pre-commit-uv pre-commit run <span style="color:#f92672">{{</span> ARGS <span style="color:#f92672">}}</span> --all-files

```

</div>After you run `chmod +x just.sh`, this file may be run using `./just.sh`, and sub-commands everything `just <subcommand>` will just work.

Please note that `--justfile just.sh` is needed if you want your Just Script to be able to introspect or call itself.

Why?
----

More and more of my clients are using Justfiles, and occasionally, I want some other recipes that may belong outside the default workflows. These can also be reusable between projects for some of my other internal tooling, so it’s an excellent resource to learn about.

Originally posted on: https://micro.webology.dev/2024/10/23/til-justfiles-can.html