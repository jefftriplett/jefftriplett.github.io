---
category: micro.blog
date: '2024-03-22T00:44:28.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: fixing-a-css-layout-issue
title: Fixing a CSS layout issue
redirect_to: https://micro.webology.dev/2024/03/21/fixing-a-css-layout-issue/
tags:
---

# 2024-03 Fixing a CSS layout issue

I noticed a layout issue for one of my website projects while viewing a page with little content. The header and footer’s background colors are dark, and the middle/main content area is white.

Where there isn’t enough content in the main/middle content area, the footer will float up, and you’ll see the white background behind it. Even if we change the default background color to match the header and the footer, the footer looks weird when stretched out.

Since I’m using [Tailwind CSS](https://tailwindcss.com), I figured there had to be a straightforward fix.

## layout.html before

I’m using Flexbox for my layout set in column mode, which allows my document to grow vertically.

```
<body class="flex flex-col">
  <header>
    our heading content
  </header>
  <main>
    our body content
  </main>
  <footer>
    our footer content
  </footer>
</body>
```

## layout.html after

My fix involved adding two classes to my html layout. The first was adding the [`min-h-screen`](https://tailwindcss.com/docs/min-height) class to the body element of my HTML document, so my page would always be at least the same height as my browser.

The second fix was adding a [`flex-grow`](https://tailwindcss.com/docs/flex-grow) class to the main element of my HTML layout. This tells the main element to fill any available space that’s left over.

```
<body class="flex flex-col min-h-screen">
  <header>
    our heading content
  </header>
  <main class="flex-grow">
    our body content
  </main>
  <footer>
    our footer content
  </footer>
</body>
```

## Overall

The fix was really straightforward. One could easily convert this to Vanilla CSS, but it’s two classes, and my content works now.
