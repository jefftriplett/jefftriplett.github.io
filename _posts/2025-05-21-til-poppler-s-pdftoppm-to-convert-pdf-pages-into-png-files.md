---
category: micro.blog
date: 2025-05-21T17:26:57.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: til-poppler-s-pdftoppm-to-convert-pdf-pages-into-png-files
title: "TIL Poppler's pdftoppm to convert PDF pages into PNG files"
redirect_to: https://micro.webology.dev/2025/05/21/til-popplers-pdftoppm-to-convert/
tags: 
---

Today I learned about [`pdftoppm`](https://www.xpdfreader.com/pdftoppm-man.html), a simple CLI tool that can convert each page of a PDF into separate image files.

My use case was to chop up a few big PDF reports to make OCR and data analysis easier, but scanning them a page at a time.

Install
-------

I’m using [Homebrew](https://brew.sh) on macOS, but Poppler will also run on Linux and other operating systems.

<div class="highlight">```shell
$ brew install poppler

```

</div>Quick Usage
-----------

<div class="highlight">```shell
$ pdftoppm -png -rx <span style="color:#ae81ff">300</span> -ry <span style="color:#ae81ff">300</span> input.pdf output

```

</div>- `-png` -&gt; save the output files as PNG images
- `-rx 300 -ry 300` -&gt; set the output resolution to 300 dpi
- `input.pdf` -&gt; your source file which you want to process
- `output` -&gt; Your output file prefix which will produce `output-1.png`, `output-2.png`, …

Originally posted on: https://micro.webology.dev/2025/05/21/til-popplers-pdftoppm-to-convert/