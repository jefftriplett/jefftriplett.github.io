---
category: micro.blog
date: 2026-02-19T14:00:00.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: jordan-baird-s-ice-beta-fixed-my-macos-tahoe-menu-bar-issues
title: "Jordan Baird's Ice beta fixed my macOS Tahoe menu bar issues"
redirect_to: https://micro.webology.dev/2026/02/19/jordan-bairds-ice-beta-fixed/
tags: 
---

If you use a Mac, you’ve probably noticed that the menu bar fills up with icons pretty quickly. [Bartender](https://www.macbartender.com) and [Ice](https://github.com/jordanbaird/Ice) (sadly, now an unfortunate name) are apps that let you manage and hide unwanted icons from your macOS menu bar so it stays clean and uncluttered.

About a year ago, I switched from Bartender to Ice, which just happens to be open source, because there was [some drama](https://micro.webology.dev/2024/06/04/bartender-mac-app.html). Since then, I’ve been very happy with Ice.

A couple of months ago, I upgraded to macOS Tahoe, and my menu bar stopped working correctly. The icon colors were all this weird shade of blue, so I couldn’t customize anything. After months of trying to figure it out, I noticed that it had been a while since Ice released a new version. That’s how open source goes sometimes.

I was getting to the point of deciding whether to go back to Bartender or stick with Ice. Today, I noticed that there’s a Homebrew package for `jordanbaird-ice@beta`. I decided to give it a try, removed the old version, installed the beta, and to my surprise and delight, the problem was fixed.

<div class="highlight">```shell
<span style="color:#75715e"># remove the stable version</span>
brew remove jordanbaird-ice

<span style="color:#75715e"># install the beta</span>
brew install jordanbaird-ice@beta

```

</div>I’m hoping there’s a more official release soon. The new Bartender looks good too, so if Ice doesn’t keep getting updated, I might switch back. If you’ve run into this same issue, give the beta a try and let me know how it goes. And if you know of any alternatives to Bartender and Ice, I’d love to hear about those too.

Originally posted on: https://micro.webology.dev/2026/02/19/jordan-bairds-ice-beta-fixed/