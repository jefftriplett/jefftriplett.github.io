---
category: micro.blog
date: 2026-02-18T22:54:47.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: my-displays-keep-rearranging-and-displayplacer-fixed-it
title: "My displays keep rearranging and displayplacer fixed it"
redirect_to: https://micro.webology.dev/2026/02/18/my-displays-keep-rearranging-and/
tags: 
---

Today I learned about [displayplacer](https://github.com/jakehilborn/displayplacer) - “macOS command line utility to configure multi-display resolutions and arrangements.”

In December, I upgraded to MacOS Tahoe and picked up the TS4 dock for my work machine.

While my upgrade was painless, the biggest issue I’ve had is with my displays. Every time my displays go to sleep and then I come back from lunch or come back the next day to work, my orientation of my displays changes and it puts them in a random order.

My displays should be arranged like this:

<div class="highlight">```shell
<span style="color:#f92672">[</span>1<span style="color:#f92672">]</span> <span style="color:#f92672">[</span>2<span style="color:#f92672">]</span>
<span style="color:#f92672">[</span>3<span style="color:#f92672">]</span> <span style="color:#f92672">[</span>4<span style="color:#f92672">]</span>

```

</div>But after waking from sleep, they end up like this:

<div class="highlight">```shell
<span style="color:#f92672">[</span>2<span style="color:#f92672">]</span> <span style="color:#f92672">[</span>1<span style="color:#f92672">]</span>
<span style="color:#f92672">[</span>3<span style="color:#f92672">]</span> <span style="color:#f92672">[</span>4<span style="color:#f92672">]</span>

```

</div>It’s really annoying. It takes a minute to fix and it’s just frustrating.

I tried displayplacer today. I had Claude Code actually run the `displayplacer list` command. It figured out which displays and which settings needed to be changed. I had it record that and then I tried it out a few times where I manually dragged my displays around, put them in the wrong order, then ran the command, and it just magically worked.

I saved the working configuration to a shell script:

<div class="highlight">```shell
<span style="color:#75715e">#!/usr/bin/env bash
</span><span style="color:#75715e"></span><span style="color:#75715e"># Restore display layout: 4 monitors (2x 16" 1920x1080, 2x 73" 2048x1280)</span>

displayplacer <span style="color:#ae81ff">\
</span><span style="color:#ae81ff"></span>  <span style="color:#e6db74">"id:F4AB0D6C-8E85-4E84-B5AB-C5B388536E3D res:1920x1080 hz:60 color_depth:8 enabled:true scaling:off origin:(0,0) degree:0"</span> <span style="color:#ae81ff">\
</span><span style="color:#ae81ff"></span>  <span style="color:#e6db74">"id:C9240C8E-A9D2-418A-89AC-28D3B5DEE5FC res:1920x1080 hz:60 color_depth:8 enabled:true scaling:off origin:(-1920,0) degree:0"</span> <span style="color:#ae81ff">\
</span><span style="color:#ae81ff"></span>  <span style="color:#e6db74">"id:B43E3352-ACB7-4163-A25B-2DDAE0174571 res:2048x1280 hz:60 color_depth:8 enabled:true scaling:off origin:(0,-1280) degree:0"</span> <span style="color:#ae81ff">\
</span><span style="color:#ae81ff"></span>  <span style="color:#e6db74">"id:B32F530C-62CF-4F0D-9997-80BF2B812AC8 res:2048x1280 hz:60 color_depth:8 enabled:true scaling:off origin:(-2048,-1280) degree:0"</span>

```

</div>I also tried setting it up as a Stream Deck key and for some reason I couldn’t get that to work. But it’s fine. I can run a shell script and that takes a lot less time to get it in the right order.

Originally posted on: https://micro.webology.dev/2026/02/18/my-displays-keep-rearranging-and/