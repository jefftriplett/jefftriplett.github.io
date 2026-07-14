---
category: micro.blog
date: '2024-04-18T02:37:05.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: starship-is-the-shell-prompt-you-have-been-looking-for
title: 🚀 Starship is the shell prompt you have been looking for 🐚
redirect_to: https://micro.webology.dev/2024/04/17/starship-is-the-shell-prompt/
tags:
- Python
- Today I Learned
---

I spent a lot of time in my shell (terminal, iTerm, bash, whatever you prefer), and by and large, my least favorite and most frustrating chore has always been trying to customize my shell prompt.

A few years ago, I tried to switch from BASH to Zsh and even the Fish Shell, and I quickly reverted because I found customizing my prompt to be such a chore.

[Starship](https://starship.rs) is one of those few life-changing development utilities that quickly solved how to customize my shell prompt. Starship also works across various shells, which means changing shells doesn’t mean starting over with a new prompt. Even though Fish and Zsh never stuck for me, Starship was a keeper.

Starship’s default prompt is really good and is a nicer starting point than Zsh or BASH gives you by default. Starship includes a bunch of default settings, which enables support for tools like aws, battery percentage, bun, git, k8s, node js, python, etc, so most of [my dotfiles config](https://github.com/jefftriplett/dotfiles/blob/main/home/.config/starship.toml) is turning off the features that I don’t care about.

There is a [Dracula Theme for Starship](https://draculatheme.com/starship), which is my go-to theme for any application that I can find that supports the color scheme.

Setting up and configuring Starship is a breeze. The documentation is clear and concise, and Starship’s settings are neatly organized in one readable and updated file, `~/.config/starship.toml`. Best of all, any changes you make are immediately applied, eliminating the need to restart your shell session. With Starship, you can confidently customize your prompt and see the results instantly.

If you use Homebrew, `brew install starship` will install it. You can activate Starship by adding `eval "$(starship init bash)"` to your `~/.bashrc` file.

If you have been thinking about trying out Starship or need help figuring out where to start or how to customize your shell prompt, I highly recommend it.
