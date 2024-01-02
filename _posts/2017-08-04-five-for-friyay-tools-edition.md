---
category: Five for Friyay
date: 2017-08-04 10:40:00 -0600
image: https://generator.opengraphimg.com/?atSymbol=true&author=webology&authorSize=text-2xl&style=modern&tags=friyay%2Ctools&title=Tools+Edition
layout: post
location: Lawrence, Kansas. United States
tags:
- friyay
- tools
title: Tools Edition
weather: 68˚F and Clear
---

One thing you quickly learn when you are a consultant/developer is to be more fluid in your tools and opinions because client opinions and practices range vastly from project to project. It can be a little intimidating at first but you can quickly learn what to compromise on (line length and git flow) vs. what to hold firm on (code quality and encouraging junior developers who learn the most from you). As soon as you get in a groove, the project may end and you have to re-adjust for the next client.

Since client setups may vary to code that runs locally, runs in a VM, runs in Docker, runs on a remote dev server, etc, I am always on the lookout for tools which can speed up one or more of this situation along with developing better practices for myself to bring to the table.

I wanted to highlight a few tools, techniques, and an article which I found to be inspiring this week.

## How to Commit

A week or two ago, I changed my commit style to use the terribly named [styleguide-git-commit-message](https://github.com/slashsBin/styleguide-git-commit-message) which is an outline for how to write useful commit messages. My favorite part of this standard is starting each commit message with a semi-meaningful emoji subject line.

I have yet to have a client ask me what I'm doing, but I have seen it subconsciously take over three projects and some of my clients adapted and starting committing with emoji leading subject lines. :sparkles: Win-win!

## One for Everyone's Toolbelt

> Seashells lets you pipe output from command-line programs to the web in real-time, even without installing any new software on your machine. You can use it to monitor long-running processes like experiments that print progress to the console. You can also use Seashells to share output with friends!

I stumbled on [Seashells](https://seashells.io/) a few weeks ago and it's completely changed how I work on remote machines.

A few weeks ago, I was working with a test suite which would only run remotely and ran through nearly 5000 tests. Trying to capture and search on the logs was a pain when something would go wrong. Seashells handled this job easily and allowed me to switch between tabs to compare results.

To use Seashells, simply install it and pipe your output to it. The utility will walk you through the rest.

Seashells is also built on the handy [xterm.js](https://github.com/sourcelair/xterm.js) library.

## Sign Your Git Commits

[keybase-gpg-github](https://github.com/pstadler/keybase-gpg-github) is an easy to follow guide on how to create a GPG key on [Keybase](https://keybase.io/) to use GPG to sign Git commits. This allows you to have verified commit messages on Github.

## Rethinking How You Teach

[Stop abusing (virtual) animals when teaching programming](https://hackernoon.com/stop-abusing-virtual-animals-when-teaching-programming-a64adc93525a) is a great think piece which recommends teaching using real examples from real projects which make teaching examples relatable. I can relate to this because I thought most of the lessons in my CS class were unrelatable which left me wondering when am I ever going to use this? Truth is, I never did.

## Guide to Live Coding on Twitch

While I have never live streamed on Twitch before, I love [Suz Hinton's](https://twitter.com/noopkat) [Lessons from my first year of live coding on Twitch](https://medium.freecodecamp.org/lessons-from-my-first-year-of-live-coding-on-twitch-41a32e2f41c1) article. It actually made me dust off a microphone I bought a few years ago and even pick up a new Logitech Webcam which just happened to be on sale when I looked. I'm not sure if I'll ever live code, but Suz's guide is just the best and I have no technical excuses for not doing so. I love it when people deep dive into their craft and explain how they do it.

*Thanks to [Heather Luna :fire:](https://twitter.com/h34th3r329) for advice on and corrections to a draft of this article. She's amazing.*
