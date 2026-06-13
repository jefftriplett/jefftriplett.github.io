---
category: micro.blog
date: 2026-06-13T16:04:52.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: how-i-work-from-anywhere-without-losing-my-place
title: "How I Work From Anywhere Without Losing My Place"
redirect_to: https://micro.webology.dev/2026/06/13/how-i-work-from-anywhere/
tags: 
---

I’ve been running a new remote development setup for the last month or so, and the goal is simple: move between all of my devices without losing my place.

The way I think about it, I have three default states:

- At my desk on my Mac Studio
- Home or out somewhere with my laptop or an iPad and a portable keyboard
- Only my phone, at practice or running errands

I wanted a setup that works across all three without rebuilding anything when I switch. I’d rather grab my iPhone or iPad with a portable keyboard than lug a laptop everywhere. If I’m at one of my kids’ practices and want to quickly follow up on something or implement an idea, I always have my phone with me.

The stack is basically:

- [Tailscale](https://tailscale.com) - glues all of my devices onto one secure network
- [tmux](https://github.com/tmux/tmux) - keeps my dev environment alive so I can leave and come back without rebuilding
- [Mosh](https://mosh.org) - keeps remote connections resilient across flaky WiFi and network changes
- [cmux](https://cmux.com) - Ghostty + Workspaces for macOS, the desktop side of this
- [Moshi](https://getmoshi.app) - the best iPhone and iPad shell I have found

The first three are the foundation. They work the same no matter which device I’m sitting at. cmux is how I connect from a desktop or laptop, and Moshi is how I connect from my phone or iPad.

Tailscale ties the machines together
------------------------------------

Start with Tailscale. I’ve used Tailscale for almost a decade because it’s free, has clients for everything like my phone, iPads, Macs, Linux boxes, and even routers and TVs. It’s a low-friction way to access all of your devices from anywhere securely and privately.

Tailscale gives me a private network across my devices, so I can connect to my Mac Studio at the office, my Mac Mini at home, my MacBook Air, and Linux boxes without opening SSH to the public internet.

That’s a big part of why I’m comfortable with this setup.

These machines are not sitting there with public SSH ports open. They’re only reachable from my tailnet. Tailscale handles the secure network piece, and I don’t have to mess with WireGuard directly.

It just works.

tmux keeps the work alive
-------------------------

tmux is the core of the setup. I’ve been running it for the last couple of months because I wanted something I could reconnect to later, similar to screen, but better suited to the way I actually work.

A lot of the time, I have something running for work, a client, or one of my own projects. I might have Django in one pane, logs in another, and Claude Code or Codex running somewhere else. With tmux, I can leave that entire development environment in place and come back to it later. Being able to do that has been worth the switch on its own.

I’m probably not using 90% of what tmux was built for. Mostly I’m using it to create sessions, connect to them, and disconnect without losing my place. I can split panes and move between them when I need to, but I find myself doing that less and less. The persistence is the part that actually matters to me.

Some alternatives to tmux are [Zellij](https://zellij.dev) and [Herdr](https://herdr.dev). I attempted to use Zellij, but struggled with the basics, so I bailed and went back to tmux. I haven’t tried Herdr, but I’ve seen people talking about it and wanted to include it.

Mosh makes remote sessions feel less fragile
--------------------------------------------

The bigger improvement came when I added Mosh.

Before I left for PyCon US, I decided I didn’t want to spend the week fighting flaky hotel, airport, and conference WiFi.

I remembered that Mosh solves a lot of the disconnect problems SSH has, so I installed it on my server, my work Mac Studio, my home Mac Mini, and my MacBook Air before I left (Homebrew on macOS, your package manager of choice on Linux).

I connected to a session before getting on the plane. About an hour into the flight, I opened my laptop, and the session resumed automatically. I didn’t have to rebuild anything or start over. It worked better than I thought it would.

Mosh and tmux make a great pair. Mosh keeps the connection resilient, and tmux keeps the actual working state alive.

On a desktop or laptop, cmux ties it together
---------------------------------------------

When I’m at a real keyboard, cmux is how I connect. It gives me Ghostty terminals and workspaces on macOS, which makes it easy to keep several machines and sessions organized at once.

Where cmux really earns its place is how it handles agents and shared sessions. One workflow I’ve come to rely on: I’ll start a tmux session on a remote machine, then connect to it in a second terminal window in cmux. Then I’ll have Claude or Codex connect to that same machine and attach to the same tmux session to do the actual work, like setting up a new Linux box or installing packages.

The nice part is that when Claude hits an interactive prompt, I can just take over the tmux session directly. I’m already attached. I can paste in API keys, answer prompts, or make changes that I wouldn’t want to hand off to an agent. Claude normally tries to handle those moments itself, and it doesn’t always do it well. This way I stay in control of the sensitive parts without losing the automation for everything else.

On my phone or iPad, Moshi is the missing piece
-----------------------------------------------

When I only have my phone or iPad with me, the part I was missing was a good way to connect to my remote sessions.

I had tried Termius before, and it was decent, but I kept running into small UI issues. CLI apps are not really designed for phones and tablets, so little things like getting to the right key at the right time can become annoying fast.

Then I tried [Moshi](https://getmoshi.app).

Moshi is an iOS and iPad app for remote terminal connections. It also runs on Apple Silicon Macs as an iPad app, which is a nice bonus.

Moshi has really good tmux support, and probably other multiplexers I haven’t tried yet. When I connect to a server that has tmux sessions running, Moshi prompts me with a list of those sessions before I even get to a shell. I don’t have to remember the command or go hunting around. I just pick the session and I’m back where I left off. That’s the feature that made the whole setup click.

Moshi also has a good mobile UI for this kind of work. I created a couple of shortcuts, one for space and one for enter, and that gets me through most of what I need when I’m using Claude Code or Codex from my phone.

Codex still has a few spots where it wants escape, and I haven’t fully figured that out yet. That may have been a connection issue, or it may be something I need to configure better.

But for most of what I’m doing, it works shockingly well. I can open my phone, connect to an existing tmux session, check logs, nudge an agent, review what changed, or keep something moving without opening my laptop.

### Setup was easier than expected

Moshi also handles setup nicely.

When you connect to a server, it can show a QR code. You scan that from your phone, and it handles creating and copying the SSH key for you.

That makes setup about as easy as I think it can be.

On Apple devices, Moshi can also share connection settings across devices on the same Apple account. Once I had it set up, connecting from my iPad was painless. I hit the button, picked my session, and I was in.

There is an Android version too. I haven’t tested it because I don’t have an Android device, but it’s there if you need it.

Moshi is a paid app, unlike the rest of this stack, which is free or open source. It runs around $30 a year or around $80 for lifetime access, which felt reasonable given how much I’m using it.

### Voice input

Moshi also supports voice input, which ended up being a bigger deal than I expected.

On my Mac, I already use voice input a lot. I use tools like MacWhisper because voice to text has become a really good input method for me.

Moshi brings that same idea to my phone and iPad.

It can use Apple’s voice to text, and it can also run a Whisper model. That means I can connect to a remote session from my phone and use voice input to interact with the tools I already have running.

Claude Code has voice support on the Mac, but that doesn’t really help when I’m remotely connected into another machine. Moshi having voice support built in makes the whole thing much more useful.

Where I’m using it
------------------

So far, I’ve been using this setup on Django TV, my job board, client work, and a bunch of one-off projects.

I have a Mac Studio at the office and a Mac Mini at home, and I’m constantly moving between them from my MacBook Air. I’ve also been playing with [direnv](https://direnv.net) so I can jump into a project and have the right environment load on the right machine. It’s not really part of this stack, but it pairs well with it.

The split helps me keep things organized. Client work lives on the Mac Studio at the office. Side projects and personal work live on the Mac Mini at home. I can connect to whichever one I need without mixing everything together on my laptop. It also helps my MacBook Air battery, because the heavier work is happening somewhere else.

And because the sessions are always running, I don’t have to worry about rebooting my MacBook Air or losing a Claude Code or Codex session mid-task. If one machine is having a problem, I can exit and switch to the other one while everything I care about stays up and running.

Review has also gotten easier. I can pull up GitHub’s web interface or the GitHub desktop app from wherever I am and review pull requests without needing my full dev environment in front of me. The work is already staged. I just need a browser.

I can still work locally when I want to. There’s nothing wrong with that. But keeping these remote sessions open all the time has been a much better experience.

The databases are already connected. The processes are already running. The agents are already in context. I can leave things in progress and come back later without rebuilding the whole setup.

The glue code
-------------

I’ve also been writing some shell aliases and scripts to smooth over the rough edges, because I don’t want to memorize tmux’s command flags.

I have a set of `tmux-*` aliases that handle the things I actually do: create a new session, resume an existing one, and kill one when I’m done. That covers most of what I need without having to look anything up.

On the cmux side, I’ve been experimenting with its CLI and API. I wrote [`cmux-dump`](https://github.com/jefftriplett/dotfiles/blob/main/home/bin/cmux-dump) and [`cmux-restore`](https://github.com/jefftriplett/dotfiles/blob/main/home/bin/cmux-restore) commands to save and reload workspace layouts. The idea is to build out profiles for each project so I can get everything running the way I want it with one command. That might mean starting a tmux session on a remote machine and connecting to it over Mosh, all from a single alias.

All of this lives in my [dotfiles repo](https://github.com/jefftriplett/dotfiles) and will keep changing as I figure out what actually works. I’m still early in this part of the setup.

When and why you need each tool
-------------------------------

You don’t have to adopt all five of these at once. Each one solves a specific problem, and you can add them as you hit that problem.

- **Tailscale** is the one to start with if your machines aren’t already on a shared network. You need it the moment you want to reach a machine that isn’t sitting in front of you without exposing SSH to the public internet. If all of your work happens on one machine, you can skip it for now.
- **tmux** is what you need when losing your terminal state hurts. If closing a laptop lid or dropping a connection means rebuilding your dev environment, restarting servers, or losing an agent session mid-task, tmux fixes that. It’s also the piece that lets two terminals, or you and an agent, share the same session.
- **Mosh** matters when your network is unreliable. Hotel WiFi, airports, conferences, tethering, or just moving between home and office. If you only ever connect over a stable wired network, plain SSH is fine. The moment you roam, Mosh is the difference between a session that survives and one you have to reconnect constantly.
- **cmux** is for the desktop side, when you’re juggling several machines and sessions and want them organized into workspaces instead of a pile of terminal windows. Any terminal works here, but cmux makes the multi-machine setup easier to live in.
- **Moshi** is for the phone and iPad side. You need it when you want to check on or nudge work from wherever you are. Its tmux session picker, key shortcuts, and voice input are what make a phone a usable terminal instead of a frustrating one.

The short version: Tailscale gets you to the machine, tmux keeps the work alive on it, Mosh keeps the connection from breaking, and cmux and Moshi are the front doors from a desk and from a phone.

This is not about working all the time
--------------------------------------

The real reason I like this setup is not because I want to maximize every spare minute of my life.

It’s almost the opposite.

This setup gives me more flexibility.

If I have 15 minutes at my son’s track meets or baseball practice, I can pull out my phone and reconnect to something already in progress. If I’m waiting on slow tests, client feedback, or a deploy, I don’t have to sit glued to my desk.

I can make dinner. I can pack lunch. I can pick up one of my kids. I can run an errand.

Then, when something is ready, I can check in, make the next change, and keep moving.

It makes the work less jarring. I don’t have to reset everything on my laptop just to make one small change or direct an agent for two minutes.

The best part is that I can just close my laptop or walk away from my desk and know that my Claude and Codex sessions are going to keep running. When I come back, whether it’s on my phone or back at my desk, I can resume right where I left off without worrying about a disconnected session or a timed-out agent.

Why this feels different
------------------------

The built-in remote options from tools like Claude Code and Codex work sometimes, but I kept running into connection weirdness when one laptop was trying to coordinate across multiple machines.

What I wanted was something that didn’t require rebuilding context every time I moved. This stack gives me that. The connection doesn’t break. The session doesn’t disappear. The agents don’t lose their place.

That’s a different kind of flexibility than I had before. It’s not about squeezing more work into more hours. It’s about not paying a tax every time I pick up where I left off.

This is what’s working well for me right now, but I’m genuinely curious what you’re using. If you have a tool that replaces one of these or collapses a few layers into one, I want to hear about it. If you try any of this and it works for you, let me know. And if I’m holding one of these tools wrong and there’s a better way, I’m all ears for that too.

---

Written by Jeff via a mix of voice transcription and typed notes. Edited with Claude Code.

Originally posted on: https://micro.webology.dev/2026/06/13/how-i-work-from-anywhere/