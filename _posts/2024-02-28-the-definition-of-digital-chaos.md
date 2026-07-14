---
category: micro.blog
date: '2024-02-28T21:35:54.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: the-definition-of-digital-chaos
title: The definition of digital chaos
redirect_to: https://micro.webology.dev/2024/02/28/the-definition-of-digital-chaos/
tags:
- Today I Learned
---

A few months ago, PayPal reached out to me via my backup email address to let me know that my primary email address no longer worked.

I knew fixing this would be painful, so I wrote down the steps as I walked through it.

## Checks Fastmail

* Logs in via 1Password
* Uses YubiKey

## Checks Cloudflare

* Logs in via 1Password
* Uses Auth app
* After logging in, I realized my domain was not hosted here.

## Checks Dynadot

* Logs in via 1Password
* Uses Auth app
* After logging in and checking my DNS settings, I realized my DNS was hosted with AWS.

## Checks AWS

* Logs in via 1Password (fails three times for Amazon security reasons)
* Uses Auth app because YubiKey fails
* Everything seems normal

## Back to Gmail

* Sends a few test emails from Gmail

## Back to Fastmail

After poking around, I noticed that Fastmail dropped my alias for “I can’t find with search reasons.”

I re-added my alias and double check that `*@domain.com` was still set to forward email.

I send a few more test emails, get a few failures, and I notice it’s back up and working again.

## Back to PayPal

* I return to PayPal to re-add my email address, which triggers another test SMS/email.
* I pull the code and re-enter into PayPal to verify my email address works again.

## Fastmail support

* I contacted Fastmail’s support, who told me this email address had never existed in their system. I have used it every month, dating back over 14 years, and it has existed since the late 90s.
* I re-create the email address.

## Back to Gmail

* I tested sending an email from Gmail again, and it works.

## Back to PayPal

* I re-try the email address from PayPal, and it works again.

## Back to Fastmail

* I re-tested from Fastmail, and now everything is working again.

## Fin

This should have ended with me throwing everything away and quitting the Internet, but here we are months later.

Instead, I have consolidated more of my DNS and domain services so that everything is easier to find and manage, but what a mess.

I lost a ton of faith in Fastmail, but I also needed more patience to push back on support to understand how and why my email forwarders and backup catchall were deleted.
