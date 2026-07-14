---
category: micro.blog
date: '2024-03-29T00:22:50.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: on-backups-and-building-a-portable-backup-drive-solution
title: On backups and building a portable backup drive solution
redirect_to: https://micro.webology.dev/2024/03/28/on-backups-and-building-a/
tags:
---

According to ChatGPT, the 3-2-1 backup rule is a simple yet effective strategy for ensuring data safety in case of a loss or disaster. Here’s what it stands for:

1. **3 copies of your data:** Maintain three copies: the original and two backups.
2. **2 different media:** Store the backups on two distinct media types or platforms.
3. **1 off-site backup:** Keep at least one backup in a different physical location.

## What this means to me

### ✅ Three copies of your data

> Maintain three copies: the original and two backups.

For our first copy, every one of my machines has hourly Time Machine backups via an external NVMe drive. These are quick, noiseless, and reliable. Even though Time Machine keeps copies through time, I consider each drive one copy since a drive can, in theory, become corrupt.

Our second to third copies are from machine to machine via Syncthing with versioning turned on. If I were to lose a machine, one to three backup copies would automatically be floating on a powered-up machine.

I keep a third remote copy on a loud Western Digital drive that I can connect for peace of mind. I also periodically clone my boot drive to this machine to have a bootable, working copy of my main work Mac and a Time Machine backup to restore from.

### ✅ Two different media

> Store the backups on two distinct media types or platforms.

My local drives are NMVe drives from two vendors. I bought them when both brands were on sale when I built my last backup drives.

I also have a Western Digital backup drive that is a noisy, spinning disk.

### ✅ One off-site backup

> Keep at least one backup in a different physical location.

My main machine runs Backblaze, giving me a nightly snapshot if I need it.

I also have Syncthing between my home and office, giving me backup copies in two physical locations.

I also keep all of my projects on GitHub and GitLab, which gives me an extra copy.

## 🧑‍🍳 My portable backup drive solution

(Links are in the parts list)

While I can’t recommend that you build your backup drive, I did out of necessity because I could not find a reasonably priced solution. I was happy with the large, clunky Western Digital external drives, but they were so loud I started looking for noiseless solutions.

After reading many reviews, I settled on the Sabrent USB-C enclosure because it is small and barely bigger than the NVMe drives. The machine powers these drives, meaning they only need one USB-C cable to connect and power them.

Based on reading review websites, I landed on the Samsung 970 EVO series drives. My first drive was a 250G drive, but I moved to 1 TB and 2 TB drives because I found them for <$100 over the holiday sales.

My go-to research tool for buying almost anything is [camelcamelcamel](https://camelcamelcamel.com). The website is free to use, and it can show you historical information so that you know if you are paying average, above, or below cost for a production on Amazon. Registering an account with them can create a price alert and get an email during a periodic sale.

**Pro tip:** When you have two young kids who keep you home on the weekends, you quickly learn that Friday nights are the cheapest day to buy just about anything. So even if camelcamelcamel doesn’t alert you, check out the website and on Amazon, and you’ll see a trend. Once again, being a parent who is home on a Friday night is an excellent life hack.

### Features of building your own

* Silent because there are no spinning disks or noisy fans
* Portable
* USB-C speed and ease
* Powered over USB-C without a clunky power supply
* They are tiny
* BYOD - Bring your own drive
* It takes less than a minute to assemble
* Cheap to build - If you buy at the right time, you can build a 1 TB or 2 TB backup drive for under <$100

### Parts list

* [SABRENT USB 3.2 10Gbps Type C Tool Free Enclosure](https://camelcamelcamel.com/product/B08RVC6F9Y) for $26 to $29
* Favorite drive: [SAMSUNG 970 EVO Plus SSD 2TB - M.2 NVMe](https://camelcamelcamel.com/product/B07MFZXR1B) for $75 to $129
* Reasonable drive: [Western Digital 2TB WD Blue SN570 NVMe](https://camelcamelcamel.com/product/B09JM8DJNS)  for $85 to $129
* Longer USB-C cable?

The USB-C cable with the SABRENT is good enough, but it’s short. It’s fine on most of my computers, but I bought a longer Anker USB-C cable for my MacBook Pro to keep it out of the way.

## Results

I didn’t expect my backup drives to work as well as they did. I tried my first one out for about a year, and then I built two more last year.
