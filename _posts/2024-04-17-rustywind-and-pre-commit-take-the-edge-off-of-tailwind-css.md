---
category: micro.blog
date: '2024-04-17T03:02:12.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: rustywind-and-pre-commit-take-the-edge-off-of-tailwind-css
title: 🧰 Rustywind and pre-commit take the edge off of Tailwind CSS
redirect_to: https://micro.webology.dev/2024/04/16/rustywind-and-precommit-take-the/
tags:
- Today I Learned
---

Last year, I wrote this [TIL: Creating a Rustywind pre-commit hook](https://jefftriplett.com/2023/rustywind-pre-commit-hook/), which illustrates how to use the [Rustywind](https://github.com/avencera/rustywind) CLI, which helps organize [Tailwind CSS](https://tailwindcss.com) classes.

Rustywind is a CSS class linting and formatting CLI tool that helps sort Tailwind CSS classes consistently and can help to de-duplicate them. If you struggle with duplicate classes or feel overwhelmed, Rustywind might be what you need.

I prefer to install Rustywind as a [pre-commit](https://pre-commit.com) hook to run on every git commit or when I run `pre-commit run`.

This `.pre-commit-config.yaml` config will run the latest version of Rustywind every time pre-commit runs.

```
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: rustywind
        name: rustywind Tailwind CSS class linter
        language: node
        additional_dependencies:
          - rustywind@latest
        entry: rustywind
        args: [--write]
        types_or: [html]
```

`pre-commit` is also an excellent way to manage your project’s other linting and formatting tools. It can be used to ensure you always use the latest version of Rustywind and other tools.
