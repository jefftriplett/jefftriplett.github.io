---
category: micro.blog
date: 2025-07-03T00:06:57.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: ditching-cloud-apis-how-i-set-up-local-text-to-speech-with-kokoro-tts-and-python
title: "Ditching Cloud APIs: How I Set Up Local Text-to-Speech with Kokoro TTS and Python"
redirect_to: https://micro.webology.dev/2025/07/02/ditching-cloud-apis-how-i/
tags:
- ai
- tts
- local-ai
- python
- automation
---

Today, I fired up the [Voices](https://github.com/nazdridoy/kokoro-tts) macOS app, which I occasionally use to convert blog posts or documentation text to audio files that I can take on the go. I usually use one of OpenAI’s Whisper APIs, but today I noticed there was a new option called Kokoro, which is a local voice model. I was interested in the model and tried out a few voices. Two or three of them were amazing for a local model.

After trying out a few blog posts and listening to them, I decided to find a Python version of the model. It might be slow to run, but at least I can create a pipeline to automate the process of generating voice files from arbitrary text files I have lying around.

That’s when I found the [Kokoro TTS](https://github.com/nazdridoy/kokoro-tts) application. I downloaded it and noticed that it needed a few things. Things like NumPy required to be installed, and a couple of things were out of sync, but the project mostly just worked. While it wasn’t quite as fast as a native Mac app, it was still good enough for me to run text files through it very quickly.

Tonight, I decided to write up my notes on how to bootstrap and run the project.

Installation
------------

<div class="highlight">```shell
git clone https://github.com/style-bert-vits2/kokoro-tts.git

cd kokoro-tts

uv add numpy

uv sync

wget https://github.com/nazdridoy/kokoro-tts/releases/download/v1.0.0/voices-v1.0.bin

wget https://github.com/nazdridoy/kokoro-tts/releases/download/v1.0.0/kokoro-v1.0.onnx

```

</div>Basic Usage
-----------

Once installed, you can use Kokoro TTS from the command line:

<div class="highlight">```shell
echo <span style="color:#e6db74">"Hello, this is a test of Kokoro TTS"</span> | ./kokoro-tts /dev/stdin example-streaming.mp3 <span style="color:#ae81ff">\
</span><span style="color:#ae81ff"></span>	--format mp3 <span style="color:#ae81ff">\
</span><span style="color:#ae81ff"></span>	--voice af_heart

```

</div>If you already have an existing text file:

<div class="highlight">```shell
./kokoro-tts textfile.txt example-textfile.mp3 <span style="color:#ae81ff">\
</span><span style="color:#ae81ff"></span>	--format mp3 <span style="color:#ae81ff">\
</span><span style="color:#ae81ff"></span>    --voice af_heart

```

</div>Conclusion
----------

Kokoro TTS is a solid local text-to-speech option that runs entirely on your machine without requiring API calls or internet connectivity. While it may not be as fast as native Mac apps, the quality is impressive for a local model, and the ability to automate voice file creation from text files makes it valuable for anyone who wants to convert written content to audio format.

One major advantage I discovered is that unlike most cloud APIs like Whisper that limit posts to around 3000 characters, Kokoro didn’t seem to have an upper limit on any of the content I tried it with. This makes it particularly useful for longer blog posts and documentation.

The setup process is straightforward once you handle the missing dependencies, and the command-line interface makes it easy to integrate into existing workflows or automation scripts.

---

*Written by Jeff. Edited with [Grammarly](https://grammarly.com) and [Claude Code](https://claude.ai/code).*

Originally posted on: https://micro.webology.dev/2025/07/02/ditching-cloud-apis-how-i/
