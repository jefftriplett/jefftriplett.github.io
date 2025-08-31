---
category: micro.blog
date: 2025-08-14T03:45:10.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: syncthing-2-0-upgrade-notes
title: "Syncthing 2.0 Upgrade Notes"
redirect_to: https://micro.webology.dev/2025/08/13/syncthing-upgrade-notes/
tags:
---

[Syncthing 2.0](https://github.com/syncthing/syncthing/releases/tag/v2.0.0) was released last week, and I upgraded my Macs and my Intel NUC. I’m pleased with the performance. I never had complaints about it being slow, but the new app is much faster. I like that they’re using a SQLite database, which makes it easier to write hacks or tools to check the data.

Upgrading wasn’t terrible. I used [Homebrew](https://brew.sh) to upgrade it, which seemed to work initially, but I had problems with the service when I restarted it. I took the following steps: stopped Syncthing, removed it, reinstalled it, and then started the service. I’ve never managed to get a service to work correctly on macOS when I write them by hand, so I let Homebrew handle the services. It understands how to write the right templates and format, and gets it right. After running these commands, everything just worked:

<div class="highlight">```shell
brew services stop syncthing  
brew remove syncthing  
brew install syncthing  
brew services start syncthing

```

</div>One pro tip: once everything has stopped, you can run `syncthing` manually instead of invoking the service to see it migrate each folder to the new SQLite database format.

I had over 100 shared folders because I was treating each of my projects and client projects as their separate shares. I’ve recently changed that and have been migrating everything into my own “Projects” folder and keeping client stuff in a “Clients” folder. That way, everything separates. I have more control over what I have on my home or personal laptop versus what I have on my work computer. This makes a nice separation of work and home life.

I prefer Syncthing over other tools because it runs well even on ancient hardware. It works on every operating system—I mostly use macOS and Linux, but I’ve even run it on a Raspberry Pi. I’m currently running it across four or five systems, which makes file sharing seamless. The sync speed is excellent, I’m not locked into any services like Dropbox, and I don’t have to pay for features I don’t need. The usability and speed hit the sweet spot for me.

My only complaint about Syncthing is the CLI experience for adding folders. Even after years of using it, I haven’t figured out if it’s possible or if I’m just doing it wrong. Maybe this changed in 2.0, but most forum discussions suggest editing the raw XML configuration directly. I only spent a few minutes looking into the 2.0 CLI, and it hasn’t clicked yet.

---

Written by Jeff. Edited with [Grammarly](https://grammarly.com) and [Claude Code](https://claude.ai/code).

Originally posted on: https://micro.webology.dev/2025/08/13/syncthing-upgrade-notes/
