---
category: micro.blog
date: 2025-01-02T15:02:42.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: my-most-used-commands-in-my-terminal-history
title: "🐚 My most used commands in my terminal history"
redirect_to: https://micro.webology.dev/2025/01/02/my-most-used-commands-in.html
tags:
---

2025-01-02 My most used commands in my terminal history
=======================================================

This post was inspired by [Andrea Grandi’s](https://mastodon.social/@andreagrandi) [My ZSH history](https://www.andreagrandi.it/posts/my-zsh-history/) post, but I modified it back to work with my customized BASH output instead

<div class="highlight">```shell
➜ history | awk <span style="color:#e6db74">'{print $4}'</span> | sort | uniq --count | sort --numeric-sort --reverse | head -10
<span style="color:#ae81ff">11063</span> git
<span style="color:#ae81ff">7636</span> just
<span style="color:#ae81ff">3280</span> cd
<span style="color:#ae81ff">2575</span> workon
<span style="color:#ae81ff">1512</span> ls
<span style="color:#ae81ff">1061</span> subl
 <span style="color:#ae81ff">967</span> docker
 <span style="color:#ae81ff">887</span> cat
 <span style="color:#ae81ff">703</span> python
 <span style="color:#ae81ff">700</span> gittower

```

</div>I guess you could say I use `git` a lot.

`just` is my main workflow driver.

`workon` - I switched between projects 2575 times.

`subl` and `gittower` are aliases to open [Sublime Text](https://www.sublimetext.com) and to open the existing project in [Git Tower](https://www.git-tower.com), respectively.

I used `docker` more than I would have guessed, but `just` tends to wrap most of that workflow, or it would have given `git` a run for its money.

Originally posted on: https://micro.webology.dev/2025/01/02/my-most-used-commands-in.html
