---
category: Five for Friyay
date: 2017-04-28 16:30:00 -0600
image: https://generator.opengraphimg.com/?atSymbol=true&author=webology&authorSize=text-2xl&style=modern&tags=friyay&title=CSS+and+HTML+Resources
layout: post
location: Naperville, Illinois United States
tags:
- friyay
title: CSS and HTML Resources
weather: 66˚F It was mostly cloudy.
---

Despite spending most of my professional time working on backend Python and API code, I try when possible to keep current on HTML5 and CSS trends. This week, I wanted to highlight some good resources which I found to be useful.

----

## What I'm learning

[Grid Garden](http://cssgridgarden.com/) by [Thomas H. Park](https://twitter.com/thomashpark) is a CSS game which teaches you how to learn CSS grid. 

I don't normally care for these types of games but I wanted an excuse to learn CSS grid and Thomas does a great job of teaching in a way that your mistakes are even educations which the grid doesn't quite work how I thought it should.

![](/assets/images/posts/friyay-css-html-resources/cssgridgarden.png)

----

## What I'm learning

[Flexbox Froggy](http://flexboxfroggy.com/) by [Thomas H. Park](https://twitter.com/thomashpark) is another CSS game which focuses on learning CSS flexbox. It's fun and I played this all the way through over lunch.

![](/assets/images/posts/friyay-css-html-resources/flexboxfroggy.png)

----

## What I'm reading

[A Field Guide to Flexbox](https://gumroad.com/l/YdWw) by [Joni Trythall](https://twitter.com/JoniTrythall) is a great pocket guide for learning CSS flexbox. My copy came in this last week and Joni teaches flexbox in a straightforward and beautifully designed visual guide.

----

## Library I'm using

I used [html-proofer](https://github.com/gjtorikian/html-proofer) on this year's [DjangoCon US website](https://2017.djangocon.us/) to help spot errors in our rendered HTML files. html-proofer [integrates easily](https://github.com/djangocon/2017.djangocon.us/blob/master/Rakefile) with [Travis CI](https://travis-ci.org/) so that we can verify that a pull request doesn't contain a broken link, image, or cause any common accessibility issue. 

Since one broken link on a header can impact dozens of pages, it's easy to start with 100s of errors. We started with almost 300 errors on the DjangoCon US website, but after 20 to 30 minutes I was down to only a few dozen errors. 

I have started using html-proofer in all of my projects as a result.

----

## Terminal application I'm using

While not exactly a frontend tool, I have found [tiny-care-terminal](https://github.com/notwaldorf/tiny-care-terminal) to be inspiring. tiny-care-terminal is "a little dashboard that tries to take care of you when you're using your terminal." Close enough ;)

<img src="https://cloud.githubusercontent.com/assets/1369170/25066240/adc3b1ac-21d5-11e7-9811-508b6bcfcc89.png" width="800"/>