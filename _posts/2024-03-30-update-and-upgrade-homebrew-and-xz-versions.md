---
category: micro.blog
date: '2024-03-30T00:00:01.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: update-and-upgrade-homebrew-and-xz-versions
title: ⬆️ Update and upgrade Homebrew and `xz` versions
redirect_to: https://micro.webology.dev/2024/03/29/update-and-upgrade-homebrew-and/
tags:
---

After I left work today, I noticed a flood of messages about a vulnerability in the `xz` package that a few dozen of my Homebrew packages used.

I find these [security alerts](https://github.com/orgs/Homebrew/discussions/5243) hard to read and understand, but here is what you need to do if you are on macOS and using Homebrew.

Thankfully, the Homebrew community already has a fix in place, and all we need to do is update Homebrew and install the latest upgrades of any packages linked/built against `xz` version `5.6.x`.

For more details, check out [Security Alert: Potential SSH Backdoor via LIBLZMA](https://hackaday.com/2024/03/29/security-alert-potential-ssh-backdoor-via-liblzma/#respond).

## Am I vulnerable?

From your terminal run:

```
brew info xz
==> xz: stable 5.4.6 (bottled)
```

If your `xz` version is 5.4.x, you are safe. 👍

If your `xz` version is 5.6.x, do not pass; go and update your Homebrew immediately. 👎

## To update your Homebrew version

```
brew update
brew upgrade

brew info xz
==> xz: stable 5.4.6 (bottled)
```

## Post Homebrew upgrade

Once you are done, I recommend rebooting your Mac and installing any recent macOS updates.
