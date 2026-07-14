---
category: micro.blog
date: '2024-02-23T19:35:08.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: three-years-later-email-is-less-of-a-pain
title: Three years later, email is less of a pain
redirect_to: https://micro.webology.dev/2024/02/23/three-years-later-email-is/
tags:
---

**Disclaimer:** Forward Email did *not* pay me to write this.

I wrote about my side projects and how [email is a pain](https://jefftriplett.com/2021/side-projects-email-is-a-pain/) a few years ago, and this morning, I saw a [Mastodon post](https://mastodon.social/@zrail@hachyderm.io/111981176443853726) that led me back here.

At the time, I ran into a point with my side projects where they would grow up and eventually need an email address dedicated to them. Instead of trying to manage a dozen email accounts, I stumbled on [Forward Email](https://forwardemail.net), and they solved the problem by allowing me to forward emails to other email accounts. Three years and annual billing cycles later, the service works.

This morning, I discovered they now support [outbound SMTP emails](https://forwardemail.net/en/guides/send-email-with-custom-domain-smtp), which allowed me to simplify how I configure and send emails for my projects. I used Mailgun and Sendgrid, but my send volume was just low enough that I struggled to keep Sendgrid from closing my account.

Forward Email also now supports [Email webhooks](https://forwardemail.net/en/free-email-webhooks), and they have an Email API, which could be handy for a few projects.

If you work on any number of side projects and you find yourself dreading email, as I did, I recommend Forward Email to at least route email to one email account while having the right dials and switches to make the experience not suck.
