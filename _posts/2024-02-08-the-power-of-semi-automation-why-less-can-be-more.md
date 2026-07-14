---
category: micro.blog
date: '2024-02-08T05:21:58.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: the-power-of-semi-automation-why-less-can-be-more
title: 'The Power of Semi-Automation: Why Less Can Be More'
redirect_to: https://micro.webology.dev/2024/02/07/the-power-of-semiautomation-why/
tags:
- Python
---

According to the [ninety-ninety rule](https://en.wikipedia.org/wiki/Ninety%E2%80%93ninety_rule), the final 10 percent of code needed to automate a task completely can take up 90 percent of the development time. This disproportionate effort is why I recommend that everyone consider semi-automating tasks and skipping the last 10%.

## Quick wins

My goal with semi-automating tasks is to reduce the scope of a project to make automating the task easier and quicker.
The more mundane and repetitive the task, the more likely I will prioritize automating it.

My favorite tasks to automate fall are quick wins or redundant processes.
We use Toggl at work to log our billable hours and time spent on various projects.
We have daily stand-ups in Slack, so everyone can keep up with everyone and be on the same page about vacations or might need another set of eyes on a project.

Using the Toggl API, I wrote a Python script that exports my notes so I can copy and paste them into Slack.
I wrote a Python stand-up script that I run daily to see my notes from the previous day or week.

I could have over-engineered my script to attempt to post to Slack for me, but it turns out that all I needed was a better way to copy and paste from Toggl into Slack.

## Why do I semi-automate tasks?

**Semi-automation is easier.** The benefit of semi-automating tasks is to reduce the scope to be a quick, productive win.

**Semi-automation saves time.** I often spend 30 minutes writing a Python script, saving me 15 minutes or more daily.

**Semi-automation saves wasted effort.** For my daily stand-up project, I can use an existing Python library to access the Toggl API and display all my entries for a day or range of dates.
Most of the time, I will copy these notes as they are and paste them into Slack, or I will summarize them.

**Semi-automation takes less maintenance.** Since my Python script is wrapping an existing API, there is little to no maintenance.
If the author decides they don’t want to maintain a Toggl library anymore, switching to another library is less effort and much less complex than if I were trying to maintain my library.

**Semi-automation is often good enough.** I thought about writing a Slackbot to post updates for me, but I quickly learned that it would be a bigger hassle and ultimately not worth the effort.
My most significant pain point was having to pull up Toggl to get information out of it, and with my stand-up script, I could focus on writing better summaries while logging my hours instead.

## Types of projects I like to semi-automate

The projects I like to semi-automate are repetitive tasks I have to do daily, weekly, and frequent enough to warrant
The more repetitive a task is, the more likely I will write a Python script or [casey/just](https://github.com/casey/just) justfile recipe to automate it.

* “copy to clipboard” page
* my daily stand-ups and monthly reports, which I pull from Toggl
* use RSS feeds to help automate the collection of articles to review for a weekly newsletter
* use justfile recipes for every project and even system-level macOS updates, so I don’t have to remember how to update or run my projects

## Migrating unfinished projects

Once I realized that some of my unfinished projects were too ambitious, I started revisiting them to reduce the scope to something I could semi-automate to complete them.
