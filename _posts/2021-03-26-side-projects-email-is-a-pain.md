---
author: Jeff Triplett
categories:
- Side Projects
category: Side Projects
date: 2021-03-26 21:38:00-06:00
excerpt: I love working on side projects, but I hate setting up and configuring email
  for projects.
image: https://generator.opengraphimg.com/?atSymbol=true&author=webology&authorSize=text-2xl&style=modern&tags=email%2Cside+projects&title=Side+Projects%3A+Email+is+a+Pain
layout: post
location: Home @ Lawrence, Kansas United States
slug: side-projects-email-is-a-pain
tags:
- email
- side projects
title: 'Side Projects: Email is a Pain'
weather: 59˚F Clear.
---

I love working on side projects, but I hate setting up and configuring email for projects.
Not only is configuration a pain, but troubleshooting and then remembering to check a dozen+ mailboxes while juggling SPAM and misclassified emails is arduous at best.

A few months ago, I saw a recommendation on Twitter for [Forward Email](https://forwardemail.net), an email forwarding service.
I decided to try it out on a whim, and I have been a happy customer ever since.

Forward Email's secret sauce is that it's configurable with just a few DNS records, and then it just works.
Setting up a new domain is as easy logging in, registering your domain, and then configuring three DNS records:

```
MX   @  mx1.forwardemail.net  10
MX   @  mx2.forwardemail.net  20
TXT  @  forward-email=you@here.com
```

Now all of my emails go to one account, and setting up a new group or alias for someone only takes me less than a minute from my Cloudflare account, which is where I manage my DNS these days.
