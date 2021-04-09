---
category: Personal
date: 2020-02-11 11:30 -0500
image: https://generator.opengraphimg.com/?atSymbol=true&author=webology&authorSize=text-2xl&style=modern&tags=&title=Keeping+Git+Forks+Updated+and+Tidy
layout: post
location: REVSYS @ Lawrence, Kansas United States
title: Keeping Git Forks Updated and Tidy
weather: 40˚F Partly Cloudy.
---

From time to time, I need the ability to track upstream changes while keeping my git commit history clean, but I can never remember how. I also want to avoid messy merge commits because those are just the worst. 

I'm going to assume that you have already forked a repository. I am going to use the `djangocon/2020.djangocon.us` repository as my example. 

## To track changes

```shell
$ git remote add upstream git@github.com:djangocon/2020.djangocon.us
```

## To update 

Every time I want to update my local `master` branch:

```shell
$ git checkout master
$ git fetch upstream
$ git rebase upstream/master
```

## To update a branch

For every branch that I want to update, I need to first check out the branch and then rebase our upstream changes to it. We will rebase against `upstream/master` vs. `master` to avoid having to rebase both `master` and our branch.

```shell
$ git checkout the-branch-to-update
$ git fetch upstream
$ git rebase upstream/master
```

**Thanks to [Lacey Williams Henschel](https://twitter.com/laceynwilliams) for advice on and corrections to a draft of this article.**