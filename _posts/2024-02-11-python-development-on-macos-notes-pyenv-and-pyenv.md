---
category: micro.blog
date: '2024-02-11T02:04:43.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: python-development-on-macos-notes-pyenv-and-pyenv
title: 'Python Development on macOS Notes: pyenv and pyenv-virtualenvwrapper'
redirect_to: https://micro.webology.dev/2024/02/10/python-development-on-macos-notes/
tags:
- Python
- Today I Learned
---

Here are my notes for using [`pyenv`](https://github.com/pyenv/pyenv) and [`pyenv-virtualenvwrapper`](https://github.com/pyenv/pyenv-virtualenvwrapper) on macOS.

I use `pyenv` to install and manage multiple Python versions on the same machine. `pyenv` makes it possible to upgrade my default version of Python without breaking every project that was created with the older version until I’m ready to upgrade them.

I use `pyenv-virtualenvwrapper` to manage my projects. `pyenv-virtualenvwrapper` is a set of tools that make it easier to create, delete, copy, and manage Python virtual environments.

## Install pyenv through Homebrew

```
brew update
brew install pyenv
brew install pyenv-virtualenvwrapper
```

## Configuring pyenv to work with my shell

```
## set a variable for finding pyenv
export PYENV_ROOT="${HOME}/.pyenv"

# 2024-02 Python  pyenv settings
if command -v pyenv > /dev/null; then
    eval "$(pyenv init --path)";
    eval "$(pyenv init -)";
    pyenv virtualenvwrapper_lazy
fi
```

## Install the “latest” Python versions using pyenv

```
# install latest Python 3.11
pyenv install 3.11:latest

# to see which version of 3.11 was installed
pyenv latest 3.11
> 3.11.7

# install latest Python 3.12
pyenv install 3.12:latest

# to see which version of 3.12 was installed
pyenv latest 3.12
> 3.12.1

# set each version globally to our latest python 3.x version
pyenv global 3.11.7 3.12.1
```

## Upgrading Python versions

```
pyenv install --skip-existing 3.11:latest
pyenv install --skip-existing 3.12:latest
```

## List every version of Python that is installable

```
pyenv install --list
```

## List every installed version of Python

```
pyenv versions
```
