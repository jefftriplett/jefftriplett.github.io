---
category: micro.blog
date: 2024-07-09T14:30:00.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: sharing-is-caring-how-a-simple-sudo-question-led-to-better-solutions
title: "🔓 Sharing is Caring: How a Simple Sudo Question Led to Better Solutions"
redirect_to: https://micro.webology.dev/2024/07/09/sharing-is-caring.html
tags:
---

One of the fun discoveries of blogging is finding your article in search results while trying to solve a problem.

A few weeks ago, I upgraded my Macs to macOS to Sonoma, but I hadn’t yet re-enabled passwordless authentication via sudo. If this were a server in the cloud, I would approach it differently, but on my laptop, it’s a different story, and I can skip re-typing my password.

I stumbled on my [TIL: Enable sudo without a password on MacOS](https://jefftriplett.com/2022/enable-sudo-without-a-password-on-macos/) post from 2022 when I was searching for a quick fix.

I also [posted on Mastodon](https://mastodon.social/@webology/112752248397936405) about this, which led to [Anthony’s](https://mastodon.social/@anthony@indieweb.social/112752290076010862) helpful [suggestion](https://sixcolors.com/post/2023/08/in-macos-sonoma-touch-id-for-sudo-can-survive-updates/) that I could instead use Touch ID which I liked a lot.

I wish I could use Touch ID, but I often use SSH and Remote Desktop. Touch ID will only work if my finger is there. It’s still an excellent suggestion for anyone seeking a more secure way to assume sudo access.

[Dan Ryan](https://mastodon.social/@d@dryan.com/112753300845939084) pointed me to a [better solution](https://apple.stackexchange.com/questions/398656/sudoers-file-resets-with-every-macos-update/398669#398669) than my existing workaround, which doesn’t get overwritten every major macOS update.

Helpful suggestions like these are why I like to think out loud and share these thoughts on Mastodon.

Originally posted on: https://micro.webology.dev/2024/07/09/sharing-is-caring.html
