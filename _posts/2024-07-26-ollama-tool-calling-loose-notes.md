---
category: micro.blog
date: 2024-07-27T04:30:18.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: ollama-tool-calling-loose-notes
title: "🦙 Ollama Tool Calling Loose Notes"
redirect_to: https://micro.webology.dev/2024/07/26/ollama-tool-calling.html
tags: 
---

I spent a [few hours this week](https://micro.webology.dev/2024/07/24/ollama-llama-red.html) working with the Ollama project and trying to get tool calling to work with the LangChain library.

Tool calling is a way to expose Python functions to a language model that allows them to be called. This will enable models to perform more complex actions and even call the outside world for more information.

I haven’t used LangChain before, and I found the whole process frustrating. The docs were full of errors. I eventually figured it out, but I was limited to one tool call per prompt, which felt broken.

Earlier today, I was telling a colleague about it, and when we got back from grabbing coffee, I thought I would check the Ollama Discord channel to see if anyone else had figured it out. To my surprise, they added and released [Tool support](https://ollama.com/blog/tool-support) last night, which allowed me to ditch LangChain altogether.

The Ollama project’s [tool calling example](https://github.com/ollama/ollama-python/blob/main/examples/tools/main.py) was just enough to help get me started.

I struggled with the function calling syntax, but after digging a bit deeper, I found this example from [OpenAI’s Function calling docs](https://platform.openai.com/docs/assistants/tools/function-calling), which matches the format the Ollama project is following. I still don’t fully understand it, but I got more functions working and verified that I can make multiple tool calls within the same prompt.

Meta’s Llama 3.1 model supports tool calling, and the two work quite well together. I am also impressed with Llama 3.1 and the large context window support. I’m running the 8B and 70B models on a Mac Studio, and they feel very close to the commercial APIs I have worked with, but I can run them locally.

Embedding models
----------------

Tonight, I tried out Ollama’s [Embedding models](https://ollama.com/blog/embedding-models) example, and while I got it working, I still need to put practical data into it to give it a better test

One more tip
------------

If you did not know Ollama can parse and return valid JSON, check out [How to get JSON response from Ollama](https://whoa.fyi/how-to-get-json-response-from-ollama/). It made my JSON parsing and responses much more reliable.

Originally posted on: https://micro.webology.dev/2024/07/26/ollama-tool-calling.html