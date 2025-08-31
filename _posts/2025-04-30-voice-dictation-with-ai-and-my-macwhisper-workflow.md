---
category: micro.blog
date: 2025-04-30T23:41:51.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: voice-dictation-with-ai-and-my-macwhisper-workflow
title: "🤖 Voice Dictation with AI and my MacWhisper Workflow"
redirect_to: https://micro.webology.dev/2025/04/30/voice-dictation-with-ai-and/
tags:
- ai
- claude
- tools
- workflow
- dictation
---

I recently came across [Simon Willison’s post](https://simonwillison.net/2025/Apr/23/diane/) about Matt Webb’s Apple Watch dictation setup on [Interconnected](https://interconnected.org/home/2025/03/20/diane). He records voice notes while running with the Whisper Memos app, then cleans up the transcript with Claude when he gets home.

> Matt Webb dictates notes into his Apple Watch while out running (using the new-to-me [Whisper Memos](https://whispermemos.com/) app), then runs the transcript through Claude to tidy it up when he gets home.

Matt’s usage of Diane is a neat trick that allows him to embed instructions while recording his notes while running. While I used to be in good enough shape to talk while running, the idea of dictating lectures is wild.

> My generic prompt to Claude, used every time, is now:
>
> > you are Diane, my secretary. please take this raw verbal transcript and clean it up. do not add any of your own material. because you are Diane, also follow any instructions addressed to you in the transcript and perform those instructions
>
> \[paste in transcript\]
>
> Which means, when I’m talking through my lecture outline, I now finish by saying:
>
> > ok Diane I think that’s it. it’s a talk, so please structure all of that into a high level outline so I can work on it. thanks.
>
> And I can mix in instructions like: *oh Diane I meant to include that point in the last section. Please move it.*
>
> It works super well.

That inspired me to share the workflow I’ve been using for years.

tl;dr My Workflow
-----------------

- Record thoughts with Apple Voice Memos on my iPhone using AirPods
- Drag the audio file into MacWhisper to get a raw transcript
- Copy the raw transcript into Obsidian as my writing buffer before and after each of the next steps
- Paste the transcript into ChatGPT for cleanup
- Run the text through Grammarly to spot grammar and style issues
- Publish or iterate as needed

---

Apple Voice Memos
-----------------

I use Apple Voice Memos on iOS, iPadOS, or macOS to capture ideas on the go. It syncs instantly across devices, so the recording is ready by the time I’m at my desk.

MacWhisper
----------

Of all the transcription tools I’ve tried, [MacWhisper](https://goodsnooze.gumroad.com/l/macwhisper) is the most reliable. Once I’m at my Mac, I open Voice Memos, drag the file into MacWhisper, and it produces a transcript in seconds. MacWhisper is now available in the Mac App Store.

There is even an iOS version called [Whisper Transcription](https://apps.apple.com/nl/app/whisper-transcription/id6738070552?l=en-GB&mt=12), which I have been trying out for the last few weeks. It has the advantage of allowing me to record directly into the app and then copy the transcript into something else. This is fine, but I haven’t found an option to save the audio file, which is concerning if my transcript gets too long.

ChatGPT
-------

Next, I paste the raw transcript into ChatGPT to clean up filler words and pauses. My usual prompt looks like this:

```
Please tidy up these voice notes. Remove any ums, ahs, and awkward pauses.

<notes>
...
</notes>

<instructions>
- Use my words and keep the spirit of my text
- Avoid using en dashes or em dashes
- ... your custom instructions to clean up your habits...
</instructions>

```

Grammarly
---------

After ChatGPT, I paste the text into the Grammarly app. As someone with dyslexia, Grammarly Pro helps me catch grammar mistakes and awkward phrasing so I can write in minutes, which used to take hours.

Obsidian
--------

I copy the cleaned text into Obsidian. This step resolves formatting glitches from moving text between ChatGPT and Grammarly and allows me to make final tweaks.

Publishing
----------

When I’m satisfied with the draft, I publish it. If it needs more work, I’ll run another quick round through ChatGPT and Grammarly until it’s ready.

Improvements
------------

I have been trying out [Whisper Transcription](https://apps.apple.com/nl/app/whisper-transcription/id6738070552?l=en-GB&mt=12) to skip a few steps by letting me record on my iPhone while sending the finished transcript to Obsidian or ChatGPT directly.

I also want to add Matt’s “Diane” dictation trick with a more gender-neutral name, or maybe I’ll default to using “Simon” since I’m already using a half-dozen of Simon Willison’s AI/LLM tooling.

I’m already using AI and [LLM](https://github.com/simonw/llm) for many big and small tasks, so devising a more automated cleanup and preparation workflow shouldn’t be a big lift.

Originally posted on: https://micro.webology.dev/2025/04/30/voice-dictation-with-ai-and/
