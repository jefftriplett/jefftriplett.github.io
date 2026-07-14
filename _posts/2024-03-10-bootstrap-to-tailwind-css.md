---
category: micro.blog
date: '2024-03-10T04:14:27.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: bootstrap-to-tailwind-css
title: Bootstrap to Tailwind CSS
redirect_to: https://micro.webology.dev/2024/03/09/bootstrap-to-tailwind-css/
tags:
- Django
- Python
---

I spent a few hours tonight weighing my options to port a few websites from Bootstrap to Tailwind CSS.

I started with what seems to be the original [`awssat/tailwindo`](https://github.com/awssat/tailwindo) project is a PHP console app whose goal was to convert any Bootstrap to Tailwind CSS and was last updated three years ago. I couldn’t get it to work from the console or via Docker, so I punted and looked at other options.

This led me to the [`node-tailwindo`](https://github.com/riazXrazor/node-tailwindo) project, which did install successfully for me. `node-tailwindo` project hadn’t been updated in six years, so much has changed in both projects.

Since `node-tailwindo` was installed successfully and seemed to run OK, I ran it on a few projects, including [Django Packages](https://djangopackages.org), and the results were not terrible. They were not amazing, but things worked.

I looked at commercial options, and they fall into either Browser Extensions that let you view an existing website with a copy/convert to Tailwind CSS option or tools that rewrite your existing CSS. Neither felt like a good option to me.

I finally did what any Python developer would and installed [BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/). Next, I wrote a script to read all the files in a template folder, and it extracted all the class attributes from the existing HTML. One hundred seventy-six unique classes later, I had my answer.

Writing my upgrade tool felt like a bigger project that I wanted to take on, but it helped me spot a few issues that `node-tailwindo` would struggle with.

This is where BeautifulSoup4 shines, and I could quickly swap out a few classes before I fed them into `node-tailwindo`, and it fixes several bugs where the project was confused by `{% block %}` and `{{ variable }}` tags/blocks.

This might be a project; I slowly update as I get bored since I can probably add and test 10 to 20 tests over lunch. For a brief minute, I debated if this would be my first Rust app. Spoiler: It is not.
