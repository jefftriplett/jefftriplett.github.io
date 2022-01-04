---
category: TIL
date: 2022-01-04 13:15:00-06:00
layout: post
location: REVSYS @ Lawrence, Kansas United States
slug: enable-sudo-without-a-password-on-macos
title: Enable sudo without a password on MacOS
weather: 45˚F Sunny.
---

For the millionth time, I upgraded macOS to the next major version (Monterey) and I had to search for how to re-enable password-less sudo'ing (don't judge me.)


1. edit `/etc/sudoers`

```shell
sudo visudo
```

2. Then find the admin group permission section:

```shell
%admin          ALL = (ALL) ALL
```

3. Change to add `NOPASSWD:`

```shell
%admin          ALL = (ALL) NOPASSWD: ALL
```

4. Profit until next year.
