---
category: micro.blog
date: '2024-03-28T02:31:40.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: on-syncthing-and-multiple-devices
title: On Syncthing and multiple devices
redirect_to: https://micro.webology.dev/2024/03/27/on-syncthing-and-multiple-devices/
tags:
---

When my son started kindergarten last year, I started experiencing a bit of “carrying things withdrawal”—for lack of a better term.

We had a good routine for his first five years and the first year and a half after my daughter was born. Every Monday, we loaded everyone’s backpacks into the car. I drove them to daycare/preschool and then went to work at the office or back home. Every Friday, we hauled the kids' stuff back. After kindergarten started, the sheer number of things multiplied to a daily backpack, water bottles, milk, and snacks, and I juggled all the things, plus carrying my one-year-old.

For years, I alternated between a backpack and a Satchel to carry my MacBook Pro to the office on days I was going in. I even picked up a much larger tote to bring everything and sort it out when we arrived.

I was burnt out on carrying things to the point that I dreamed of not having to bring anything with me except for my iPhone and my keys.

I was overdue for a new work machine, so I used this as an excuse to try a Mac desktop. For the office, I switched to a Mac Studio. For my home office, I picked up a Mac Mini Pro. I started using my MacBook Pro as a floater around the house and taking trips with me.

## Syncing files

My only pain point was keeping files and projects synced between machines. I already use Apple’s iCloud/iDisk, which takes care of my documents and random desktop files, but I wanted something else that wasn’t Dropbox to keep my development projects always in sync.

I’ve been using [Tailscale](https://tailscale.com) for a few years. It creates a virtual network that allows all my devices and machines to see each other regardless of location.

I tried several file-syncing solutions before landing on Syncthing, which is also open-source. Syncthing appealed to me because it’s a peer-to-peer application that doesn’t require a server to run.

I wanted control over where my data was physically located, which ruled out Dropbox, iDisk, and others. Most of my projects sync from upstairs to downstairs, and no company’s business model sits between me and my data.

Because all my projects are folder-based, I can share each project folder and choose which machine should have access to them. The process is more manual than I’d like, but it’s quick, and everything works. This also allows me to control where work and personal files are synced.

## Hardware

I’m running Syncthing on four physical machines, which include three Macs and one Intel NUC. My NUC is my main distribution point and is wired directly into my home router, whereas my Macs are connected wirelessly.

## Setup

Setup is a breeze on Linux and macOS and only takes a few seconds with your favorite package manager. Once you install Syncthing, you can run the service and copy a key, which you can share with your other nodes so they can communicate and share files.

The only annoying part is keeping my `.stignore` files in sync when I find a new pattern. While I primarily develop on M2 Macs, my MacBook Pro is an Intel model. I occasionally run into a weird issue from a cache file tied to one architecture over another.

So far, I have landed on:

```
# .stignore
*.pyc
*.pyi
.*cache/
.DS_Store
.envrc
.nox/
.vendor/
docker-compose.override.yml
```

I wanted my `.git` folder excluded from syncing, but I changed my mind. It’s nice to be on the same branch, no matter which machine I’m developing on.

## The results

My transition back to a desktop machine was 100% worth it. As long as I have my keys and iPhone, I have everything I need to be productive.

I have never noticed any latency or file syncing delays between devices. It takes less time than it takes me to walk up or down stairs to switch between devices, so that’s a win in my book.

## Bonus

I also run Tailscale’s [golink](https://github.com/tailscale/golink) private short link service on my NUC, which makes remembering how to access Syncing things easier.

http://go/syncthing will redirect me to http://127.0.0.1:8384 no matter which machine I’m on. I never have to remember which port Syncthing’s web interface runs on again.
