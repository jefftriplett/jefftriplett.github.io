---
category: micro.blog
date: '2024-02-27T01:15:29.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: things-i-do-every-time-i-start-a-django-project
title: Things I do every time I start a Django project
redirect_to: https://micro.webology.dev/2024/02/26/things-i-do-every-time/
tags:
- Django
- Python
- Today I Learned
---

In the spirit of Brenton Cleeland’s [Six things I do every time I start a Django project](https://brntn.me/blog/six-things-i-do-every-time-i-start-a-django-project/), my goal is to document and share my process since this often comes up.

Like Brenton, I have a lot of projects, and their scope may range from quick one-offs that might last a few hours to projects I have worked on for a decade or more.

## Overview and upfront notes

I use [pyenv](https://github.com/pyenv/pyenv) to manage my Python versions, but I don’t go into any details here.

I use [pyenv-virtualenvwrapper](https://github.com/pyenv/pyenv-virtualenvwrapper) to manage what Python calls a “virtual environment,” which copies and symlinks files and folders where they need to be so that your Python projects are isolated from one another.

`pyenv-virtualenvwrapper` is also a `pyenv`-friendly fork of [virtualenvwrapper](https://github.com/python-virtualenvwrapper/virtualenvwrapper).

**Please note:** To avoid even more confusion, please assume that at any time in this article, when I mention `virtualenvwrapper` or its various commands, I mean the `pyenv-virtualenvwrapper` version of these tools.

For more detail, see my article [Python Development on macOS Notes: pyenv and pyenv-virtualenvwrapper](https://micro.webology.dev/2024/02/10/python-development-on.html).

## Creating a new project

First, I need a folder to store all my project files. One nice feature of `virtualenvwrapper` is it can manage both my virtualenvs and where my projects live.

So my first step for a new project is to run `mkvirtualenv {project_name}`, where `project_name` is the name of the domain name or client that I’m working with. `mkvirtualenv` will then create a new virtual environment (`virtualenv` or `venv` is fine too) for me, make a new project folder for me to put my files into, and then transport me to this new project folder.

`virtualenvwrapper` also supports custom hooks, which is a fancy way of saying it runs a series of commands I tell it I want to run after it creates a `virtualenv`. These are a few of the custom steps that I run for my projects:

* Create a [Sublime Text](https://www.sublimetext.com/blog/articles/sublime-text-4) project file so [Alfred](https://www.alfredapp.com/) can detect it.
* Create a [Sublime Text](https://www.sublimetext.com/blog/articles/sublime-text-4) `pyrightconfig.json` file, which enables LSP support for the project so that my code autocompletion works.
* Create a [Syncthing](https://syncthing.net) `.stignore` file.
* Create a [direnv](https://direnv.net) `.envrc` file that loads my project’s environment variables.
* Transports me into my projects folder.
* Activate the new `virtualenv`, so Python is ready.
* Install the latest version of `pip`, Python’s package manager.
* Install the latest version of [pip-tools](https://github.com/jazzband/pip-tools/), which I like to use for managing my project Python requirements.
* **Soon:** Install the latest version of [uv](https://github.com/astral-sh/uv), which will soon replace pip-tools for me.

Even though most of my projects use Docker Compose, I still install my Python dependencies outside of Docker in the virtual environment so that my text editors and [pyright](https://github.com/microsoft/pyright) can read them.

## Create my Django app

Once I have a project folder and `virtualenv` set up, I must create a Django project.
I use either my [django-startproject](https://github.com/jefftriplett/django-startproject) or [REVSYS](https://revsys.com)’s Django starter template, which we call AlphaKit.
Both projects aim to start jumpstart development and spend zero time configuring projects.
Since my stater project is public, I will run this snippet to jumpstart it.

```
django-admin startproject \
    --extension=ini,py,yml \
    --template=https://github.com/jefftriplett/django-startproject/archive/main.zip \
    config
```

I landed on `config` for my projects because I like consistency when switching between projects, and over a decade and a half, I have never had a naming collision with config. The name config tends to sort to the top of my folder listings, making copying and pasting configs from project to project easier.

## Setup Git

1. Now that I have my project started, I will run `git init` inside the project folder.
2. `bunx gitignore python` to set standard files to ignore
3. I will create a new repo on Git(Hub|Lab) and set it as a remote source for my project
4. I will run `gittower .`, select which files I’m ready to commit, and write my initial commit message.
5. I will `git push` from my terminal or [GitTower](https://www.git-tower.com/mac) and confirm that my new project is set up.

## Switching projects

When I want to work on an existing project, I use `virtualenv`’s `workon` command to switch projects. `workon {project_name}` will transport me to the correct project folder and will activate my Python virtual environment so that I’m ready to work.

## Do I need templates?

If my project needs templates, I’ll use a starter `templates/base.html` and the [Tailwind CSS Play CDN](https://tailwindcss.com/docs/installation/play-cdn).

I am a few years into using Tailwind CSS, and it’s my first choice for quickly bootstrapping a project. Despite the masto-hate, Tailwind CSS works for me and is vanilla CSS-friendly.

I like their Play CDN because I can start fiddling with Tailwind CSS with zero runtime and only one script tag to include in my HTML docs head.
