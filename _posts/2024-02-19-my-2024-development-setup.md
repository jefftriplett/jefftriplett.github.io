---
category: micro.blog
date: '2024-02-19T03:39:06.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: my-2024-development-setup
title: My 2024 Development Setup
redirect_to: https://micro.webology.dev/2024/02/18/my-development-setup/
tags:
- Django
- Python
---

I have wanted to document my development setup for a while to revisit it from time to time to see how my setup changes.

## Hardware

I’m typing this from my couch on a MacBook Pro Intel/2019 model in Lawrence, KS.

I’m using a Mac Studio (M2/2023 model) at my office.

I’m using a Mac Mini Pro (M2/2023 model) in my home office.

I’m using an Intel Skull NUC (2017) and several Raspberry Pis (3s and 4s) wired to my router.

After a few decades of working on a laptop, I recently switched to a desktop machine because I wanted to sit down at either machine and work without carrying anything around. With two kids, I’m also juggling backpacks, water bottles, and whatever they need at school or preschool that day. Not having to worry about carrying anything is a huge mental weight off my shoulders.

At home, I run three Dell S2722QC 27-inch 4K USB-C monitors and a 16" portable monitor that I use as a dedicated iTerm display. At work, I use a pair of Monoprice 30" monitors and another 16" portable monitor for iTerm. At some point, I want to pick up the same Dell monitors for work.

## Software

Since 2007, I have preferred developing on macOS. I’m running on macOS Ventura on everything, but I plan to migrate to macOS Sonoma sooner rather than later.

I use [Tailscale](https://tailscale.com), so I can connect to any of my machines from anywhere. I can even connect from my iPhone or an iPad. If you have more than one machine, even if that machine is a Raspberry Pi, Tailscale is worth the ~5-minute install.

I use [Alfred](https://www.alfredapp.com), with some custom plugins, as my go-to “do everything on macOS” tool of choice.

## Themes

[Dracula](https://draculatheme.com/) is my favorite theme because it looks nice, and the community has built a theme for everything.

## Home

I run [Home Assistant](https://www.home-assistant.io) at home and have a love/meh relationship with it. I have a liberal usage of [Wyze cameras and gear](https://www.wyze.com), doubling as kid/baby monitors and external perimeter coverage around our gates and cars.

## Backups

Backups should be handled in layers:

* Quick local backups: Every Mac runs TimeMachine and backups to an encrypted, external drive. I built my NVMe backup drive solution that I will write about sometime.
* External, off-sight backups: I store external copies of my data on [BackBlaze](https://www.backblaze.com).
* I keep a few big, noisy 8TB external backup drives for occasional snapshots.

## File Syncing

* My documents are backed up to iCloud.
* I use [Syncthing](https://syncthing.net) to sync my Macs and NUC. I use this to sync projects across machines.

## Development

[SublimeText](https://www.sublimetext.com) is my go-to text/code editor. Search is blazingly fast, runs amazingly well on both old and new hardware, and is a stable product.

Almost every Django project I work on runs in a container using [Docker Compose](https://docs.docker.com/compose/) or [Orbstack](https://orbstack.dev). Orbstack is nice and fast, but I have many legacy projects in Docker, and the migration only worked so well.

I use the [“scripts to rule them all”](https://github.com/github/scripts-to-rule-them-all) pattern because I work on tons of projects, and I never want to think twice about how to start, stop, update, open a console/shell, etc, and it does the job nicely. I will write about this later.

I prefer to script project workflows using [Just](https://github.com/casey/just) because it’s a one-file install that doesn’t require a large development stack. It runs well both inside and outside of a container.

I wrote another post about [Python Development on macOS Notes: pyenv and pyenv-virtualenvwrapper](https://micro.webology.dev/2024/02/10/python-development-on.html) setup.

I use [direnv](https://direnv.net) to manage my environment variables.

## Conclusion

Overall, I’m pretty happy with everything. I would like the same Dell monitor setup for the office and a TS4 dock, but everything works.
