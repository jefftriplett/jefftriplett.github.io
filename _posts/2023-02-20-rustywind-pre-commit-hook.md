---
category: TIL
date: 2023-02-20 15:23:30-06:00
layout: post
location: REVSYS @ Lawrence, Kansas United States
slug: rustywind-pre-commit-hook
tags:
- rustywind
- tailwindcss
- pre-commit
- pre-commit hooks
title: Creating a Rustywind pre-commit hook
updated: 2024-01-02 09:05:00-06:00
weather: 62˚F Mostly Sunny
---

Thanks to Adam Johnson's [pre-commit: How to create hooks for unsupported tools](https://adamj.eu/tech/2023/02/09/pre-commit-hooks-unsupported-tools/).
I created a [pre-commit](https://pre-commit.com/) hook for [rustywind](https://github.com/avencera/rustywind), which is a CLI tool that organizes, lints, and sorts [Tailwind CSS](https://tailwindcss.com/) classes.

If you are comfortable with pre-commit, this should be a copy and paste for you to have nicely formatted Tailwind CSS linting/auto-formatting. 

```yaml
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
