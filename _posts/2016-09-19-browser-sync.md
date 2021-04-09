---
category: TIL
date: 2016-09-19
image: https://generator.opengraphimg.com/?atSymbol=true&author=webology&authorSize=text-2xl&tags=js%2Cnode%2Cnpm%2Cproxy&title=Use+%60browser-sync%60+as+a+proxy
layout: post
location: Lawrence, Kansas United States
tags:
- js
- node
- npm
- proxy
title: Use `browser-sync` as a proxy
weather: It was 89.2°F. The breeze was light.
---

I knew [`browser-sync`](https://www.browsersync.io/) was handy for working with static files, but what I didn't realize was that `browser-sync` had a proxy mode which will work with any framework.

```bash
$ npm install -g browser-sync
$ browser-sync start --files "_site/*" --proxy "localhost:8000" --reloadDelay "1000"
```

This is really handy for working with dynamic websites built with Django when you want to reload a page after you have made a template or CSS change.