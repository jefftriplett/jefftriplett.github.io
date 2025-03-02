---
category: micro.blog
date: 2025-03-02T19:34:36.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: agents-are-cheat-codes
title: "🤖 "Agents" are Cheat Codes"
redirect_to: https://micro.webology.dev/2025/03/02/agents-are-cheat-codes/
tags: 
---

Lately, I have been trying to wrap my brain around AI Agents, so as a starting point, I have been using [Pydantic AI’s Agent](https://ai.pydantic.dev/agents/) class/framework to build “Agents”.

“Agent” is a loaded term. Pydantic AI’s usage is more or less a system prompt and a good API around adding tool calls and working with existing LLMs.

I have written several experimental projects to help me quickly research and find answers to several areas of Django that confuse people, including myself. These ask-one-question bots do their best to fetch the resources they need to answer your questions.

The three I have published publicly are:

- [Django Trademark Agent](https://github.com/jefftriplett/django-trademark-agent)
- [Django Bylaws Agent](https://github.com/jefftriplett/django-bylaws-agent)
- [Django DEP-10 and DEP-12 Agent](https://github.com/jefftriplett/django-dep-10-12-agent)

None of these are official resources of the Django Software Foundation, nor should they be considered “official” or even “legal” answers to any questions that may arise.

The pattern I landed on for building the system prompts and pulling remote data has been a practical, quick way for me to get feedback and ask questions based on our existing material. I can change a local copy of the bylaws and then ask the Agent questions to see if my potential changes might be comprehensive enough for the Agent to answer.

It effectively feels like running tests on governance to see if the Agent picks up on my changes.

Our Cheat Codes
---------------

These are cheat codes for a quick one-file Agent that one can quickly stand up and ask questions.

- UV is a cheat code because it can quickly create a one-file Agent with dependencies and the version of Python needed to run the demo baked in.
- Pydantic AI’s Agent class is a nice wrapper around a system prompt and can even create a dynamic system prompt. Having a global system prompt has a nice feel to it too.
- Pydantic’s `BaseModel` creates structured data responses as a cheat code for processing unstructured text. If you haven’t seen this pattern yet, you can’t unsee it.
- The Jina AI for cleaning up HTML into Markdown is an AI I have wanted for a decade+. I use it in dozens of apps for free, saving me hours of work.
- The Python libraries Typer, Rich, and httpx may not seem like they are doing much, and I’m underutilizing them, but their Developer Experience (DX) is great, and they just work.

More areas to explore
---------------------

Pydantic AI supports dynamic [System Prompts](https://ai.pydantic.dev/agents/#system-prompts), which might save me a few extra templating steps. They didn’t really click for me before I was writing this post.

When I wrote my Django Agents, I had Pydantic AI’s [Multi-agent Applications](https://ai.pydantic.dev/multi-agent-applications/) feature in mind. In theory, I want to ask my Django Agents a question and have it route my question to the appropriate Agent to get an answer.

[Function Tools](https://ai.pydantic.dev/tools/) or Tool Call is what inspired me to try out Pydantic AI. Function Tools are a way to give LLMs the ability to get information outside of their memory and system prompts when needed. I built one for reading and writing to my work calendar to help me manage my schedule. I didn’t use them for my suite of Django Agents, but when mixed with more real-time data they could be helpful.

We could also refactor each Agent using a reusable tool call so we could assemble one Agent that can gather the information needed to answer common Django Governance questions. I don’t know if that would be effective. In theory, it might not be a bad fit after looking at their [DuckDuckGoSearchTool](https://github.com/pydantic/pydantic-ai/blob/main/pydantic_ai_slim/pydantic_ai/common_tools/duckduckgo.py) example.

Originally posted on: https://micro.webology.dev/2025/03/02/agents-are-cheat-codes/