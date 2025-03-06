---
category: micro.blog
date: 2025-03-06T00:57:07.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: ideas-for-the-levels-of-claude-notes
title: "🤖 Ideas for "The Levels of Claude" Notes"
redirect_to: https://micro.webology.dev/2025/03/05/ideas-for-the-levels-of/
tags: 
---

Lately, I have been conversing more with friends, colleagues, clients, and online friends about Claude and coding tools.

It turns out that everyone considers Claude to be something different when they ask, “Have you tried out Claude 3.7 Sonnet?” and that could mean through the website or the mobile app or people who are using it to write code or who are developing against one of Claude’s many REST APIs. Some people primarily interact with Claude by speaking in their voices while walking outside with their pets.

I have even struggled to land at a good starting point, so I have been thinking through the various ways to explain how one might use Claude.

- You can access Claude Chat through the website.
- You can access Claude through the mobile app and use voice support.
- You can copy one or more files into Claude.
- You can access Claude through an IDE.
- You use Claude Projects to organize your projects and might even have a support document you give Claude for more context.
- You can access Claude through the Claude Desktop app and use voice support.
- You have enabled MCP plugins/servers within the Claude Desktop app.
- You can access the Claude Code CLI/terminal app.
- You have enabled MCP with the Claude Code CLI/terminal app.
- You are writing your own MCP servers in Python or JavaScript.
- You have registered for Claude API access and are writing code against one of their REST APIs. (more on this later)

I originally broke this down into five levels of Claude, but there were too many platforms and features that blurred together.

Accessing Claude
----------------

Accessing Claude can be confusing because there are many ways to access it.

- Web interface
- Mobile app
- Desktop app
- CLI/Terminal app
- REST API (could be a third-party app too, that requires a developer token)

Organization by experience level
--------------------------------

If we break these down by user experience or technical proficiency:

- **Beginner**: Web interface, mobile app, IDE integrations
- **Intermediate**: Desktop app, file uploads, REST API integration
- **Advanced**: Claude Code CLI
- **Really Advanced**: You are writing custom MCP implementations.

Claude’s developer APIs
-----------------------

Claude’s Developer APIs have their vibes and are helpful in various situations. I’m not going to deep dive into them, but from a bird’s eye view:

- Text Completion API
- Embeddings API
- Messages API
- Claude-in-the-Middle (Tools API and Agents)
- Batch API

These APIs can also vary based on passing them text, documents, images, or other types of files.

I’m still amazed that I can send an image to Claude and ask it to give me back an HTML file and CSS, and it does a relatively decent job.

Conclusion: Claude as a Spectrum
--------------------------------

I wasn’t sure how to end my notes, but I asked Claude to: “Please write a conclusion about Claude being more of a spectrum than just a service.” and this is what it told me:

> When discussing “Claude,” we’re not just talking about a single AI service but rather a spectrum of capabilities, interfaces, and integration points that serve different user needs, technical abilities, and use cases.

> What makes this spectrum particularly interesting is how it creates different experiences and understanding of what “Claude” actually is. For a casual user accessing the web interface, Claude is simply a helpful chat assistant. For a developer using the API or building MCP servers, Claude becomes an extensible AI platform with programmable capabilities.

> This spectrum explains why conversations about Claude can sometimes feel like people are talking about entirely different products. In a very real sense, they are. The Claude that helps a writer craft a story through the mobile app exists in a different context than the Claude that helps a developer debug code through an IDE integration.

> As the Claude ecosystem continues to evolve, this spectrum will likely expand further, with new interfaces, capabilities, and integration points creating even more varied experiences. Understanding Claude as a spectrum rather than a singular service helps contextualize these different experiences and provides a framework for navigating the growing complexity of AI assistants.

> The most powerful aspect of this spectrum may be that it allows Claude to meet users where they are - from the casual web user to the advanced developer building custom AI solutions. This flexibility transforms Claude from merely an AI service into an adaptable AI ecosystem that can evolve alongside user needs and technical capabilities.

It’s not half bad.

Originally posted on: https://micro.webology.dev/2025/03/05/ideas-for-the-levels-of/