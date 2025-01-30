---
category: micro.blog
date: 2025-01-30T00:46:04.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: my-big-list-of-ai-llm-tools-notes-and-how-i-m-using-them
title: "🤖 My big list of AI/LLM tools, notes, and how I'm using them"
redirect_to: https://micro.webology.dev/2025/01/29/my-big-list-of-aillm/
tags: 
---

I have been using, working, and running commercial and local LLMs for years, but I never got around to sharing the tools and applications I use. Here are some quick notes, tools, and resources I have landed on and use daily.

Mac Apps I use:
---------------

I do all of my development on Macs. These tools make running local LLMs accessible.

- [Ollama](https://ollama.com) is the server that can download and run 100s of AI models.
- [Ollamac](https://github.com/kevinhermawan/Ollamac) is a GUI client for Ollama that lets you write prompts, save history, and allow you to pick models to test out quickly.
- [Tailscale](https://tailscale.com) I use Tailscale on all of my devices, which gives me access to my work M2 Mac Studio and home office Mac Mini Pro, which both run Ollama, from anywhere in the world. This makes prototyping at home quick but then I can run a larger model from my work machine and it’s so fast, it feels like the machine is running in my house.
- [OpenAI Bundle](https://goodsnooze.gumroad.com/l/openai-bundle)—I bought this bundle because it was the cheapest way to get a bunch of AI apps, including four of Jordi Bruin’s apps. I have used these for a few years.
    
    
    - [MacWhisper](https://goodsnooze.gumroad.com/l/macwhisper) - I use MacWhisper to turn voice notes and podcasts into plain text files for my notes and sometimes blog articles.
    - [Voices](https://goodsnooze.gumroad.com/l/voices) - I use Voices when I find a large blog post and want to listen to it while working.
- [Claude for Desktop](https://claude.ai/download) gets a lot of crap for being “yet another Electron app” instead of a custom-built macOS app, but the people saying that don’t know what they are talking about. The Claude Desktop has voice support and keyboard hotkeys, which make the app incredibly useful. More importantly, Claude Desktop also supports [Model Context Protocol](https://modelcontextprotocol.io), which lets Claude access your file system, git, and anything else you want to access. It’s incredibly powerful, and there’s nothing quite like it.

Baseline rules for running a model
----------------------------------

While running models locally is possible, consumer hardware is constrained by RAM and GPU for even the most miniature models. The easiest mental model to work with is that Billions of parameters are roughly equivalent to your system’s RAM in Gigabytes. An 8B model needs roughly 8G RAM to fit into memory.

My mental formula is somewhat lossy because 40B models fit 32G of memory, and 72B models fit 64G of memory with some room to spare. This is just the rough estimate that I use.

Even though you can run models locally, even the smallest models with a significant context window will exceed your machine’s available RAM. A 128k context window needs about 64 GB of RAM to load into memory for an 8B parameter model fully, even though the model can easily fit into 8GB of RAM. That doesn’t mean the model won’t run locally, but it will run closer than it would if you have more than 72 GB of RAM, which your model fully needs to fit.

I look for three things when I’m evaluating a model:

- A number of parameters are measured in Billions.
- Context length 
    - The input context length, which effectively the model’s memory
    - The output context length, which is how big the answer can be
- The type of model: 
    - **Default Models** are general-purpose models like GPT-4 and Llama 3.3.
    - **Vision Models** and process and read visual data like images and videos.
    - **Tool Models** can call external tools and APIs and perform custom actions to which you give them access.
    - **Embedding Models** can turn text into vectors or tokens, which helps measure your prompts and other RAG operations.

What about quantization? Quantization can help you scale a model down so that it might fit into memory, but there’s always a loss in quality, which defeats the purpose of using the bigger model in my book.

Keeping up
----------

My favorite resource for keeping up is [Ollama’s Models page sorted by Newest](https://ollama.com/search?o=newest) models. I check it a few times a day and you’ll see new models release single-digit hours to days before press releases can catch up.

I like [Matt Williams'](https://www.youtube.com/@technovangelist) YouTube Channel a lot. It’s the one channel I come back to, and I find that I always learn something from it. His videos tend to be ten to twenty minutes long, which is about right since the material is so dense.

Start with his [Optimize Your AI Models](https://www.youtube.com/watch?v=QfFRNF5AhME) videos. They’re a lot to fit in your brain, but they’re a great starting point.

[Simon Willison’s Weblog](https://simonwillison.net) is good too.

Python
------

I’ll have to write a few posts on how I’m using LLMs with code, but Simon’s [LLM](https://llm.datasette.io/en/stable/) is a good general-purpose AI hammer if you need one.

As of last week, I’m using [Pydantic AI](https://ai.pydantic.dev) instead of OpenAI’s or Anthropic’s Python libraries. Pydantic AI will install both of those libraries for you, but I find it to be 100% better and easier to switch between models using it than LangChain (not linked) or anything else I have tried.

Originally posted on: https://micro.webology.dev/2025/01/29/my-big-list-of-aillm/