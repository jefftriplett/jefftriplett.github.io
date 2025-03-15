---
category: micro.blog
date: 2024-06-12T02:57:51.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: exploring-ollama-an-open-source-llm-my-notes
title: "📓 Exploring Ollama: An Open-Source LLM (my notes)"
redirect_to: https://micro.webology.dev/2024/06/11/exploring-ollama-an.html
tags:
---

I have meant to do a proper write-up on the [Ollama](https://ollama.com) project for a while. Instead of putting it off any longer, I decided to publish my outline and notes, hoping that someone might find it helpful if you wanted to run your own local, offline LLM.

Why Ollama?
-----------

- Open-source LLM server
- Runs over two dozen models, with new ones released every week
- My personal favorite: [Ollama](https://ollama.com)

My Journey with Ollama
----------------------

- Discovered Ollama a year ago
- One of the first accessible projects for M-series Mac
- User-friendly and performed well.

Ollama’s Growing Compatibility
------------------------------

- Expanded to support Windows and Linux
- Became AMD-friendly
- More accessible to users with various hardware setups

The Llama3 model changes everything
-----------------------------------

- [Llama3](https://ollama.com/library/llama3) 70b model introduction
- 70b model runs on Mac Studio with 64 GB of RAM
- Enables running a powerful LLM locally
- Benefits: privacy, customization, offline access

Making Life Easier with the LLM Python Project
----------------------------------------------

- Installed [llm-ollama](https://github.com/taketwo/llm-ollama) plugin into [LLM](https://github.com/simonw/llm) Python project
- Simplifies switching between different LLMs
- Quicker and easier testing of new models compared to Ollama’s CLI

Ollama’s Library and APIs
-------------------------

- [ollama-python](https://github.com/ollama/ollama-python) library for integrating Ollama models into Python projects
- Ollama’s built-in [OpenAI compatible API](https://github.com/ollama/ollama/blob/main/docs/openai.md) for seamless use with existing OpenAI-based applications

Final Thoughts
--------------

- Ollama: a top choice for open-source, locally-run LLM
- Expanding compatibility
- Impressive Llama3 model
- Easy integration with LLM Python project
- Handy libraries and APIs
- Recommended for researchers, developers, and curious individuals

Originally posted on: https://micro.webology.dev/2024/06/11/exploring-ollama-an.html
