---
category: micro.blog
date: 2024-07-24T18:02:09.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: ollama-llama-3-1-red-pajama
title: "🦙 Ollama Llama 3.1 Red Pajama"
redirect_to: https://micro.webology.dev/2024/07/24/ollama-llama-red.html
tags: 
---

For a few weeks, I told friends I was excited to see if the new Llama 3.1 release was as good as it was being hyped.

Yesterday, Llama 3.1 was released, and I was impressed that the [Ollama](https://ollama.com) project published a release to [Homebrew](https://brew.sh) and had the models ready to use.

<div class="highlight">```shell
➜ brew install ollama

➜ ollama serve

<span style="color:#75715e"># (optionally) I run Ollama as a background service</span>
➜ brew services start ollama

<span style="color:#75715e"># This takes a while (defaults to the llama3.1:8b model)</span>
➜ ollama pull llama3.1:latest 

<span style="color:#75715e"># (optional) This takes a longer time</span>
➜ ollama pull llama3.1:70b

<span style="color:#75715e"># (optional) This takes so long that I skipped it and ordered a CAT6 cable...</span>
<span style="color:#75715e"># ollama pull llama3.1:405b</span>

```

</div>To use chat with the model, you use the same `ollama` console command:

<div class="highlight">```shell
➜ ollama run llama3.1:latest
>>> how much is 2+2?
The answer to <span style="color:#ae81ff">2</span> + <span style="color:#ae81ff">2</span> is:
4!<span style="color:#e6db74">```</span>

<span style="color:#75715e">## Accessing Ollama Llama 3.1 with Python</span>

The Ollama project has an <span style="color:#f92672">[</span><span style="color:#e6db74">`</span>ollama-python<span style="color:#e6db74">`</span><span style="color:#f92672">](</span>https://github.com/ollama/ollama-python<span style="color:#f92672">)</span> library, which I use to build applications. 

My demo has a bit of flare because there are a few options, like <span style="color:#e6db74">`</span>--stream,<span style="color:#e6db74">`</span> that improve the quality of life <span style="color:#66d9ef">while</span> waiting <span style="color:#66d9ef">for</span> Ollama to <span style="color:#66d9ef">return</span> results. 

<span style="color:#e6db74">```</span>python
<span style="color:#75715e"># hello-llama.py</span>
import typer

from enum import Enum
from ollama import Client
from rich import print


class Host<span style="color:#f92672">(</span>str, Enum<span style="color:#f92672">)</span>:
    local <span style="color:#f92672">=</span> <span style="color:#e6db74">"http://127.0.0.1:11434"</span>
    the_office <span style="color:#f92672">=</span> <span style="color:#e6db74">"http://the-office:11434"</span>


class ModelChoices<span style="color:#f92672">(</span>str, Enum<span style="color:#f92672">)</span>:
    llama31 <span style="color:#f92672">=</span> <span style="color:#e6db74">"llama3.1:latest"</span>
    llama31_70b <span style="color:#f92672">=</span> <span style="color:#e6db74">"llama3.1:70b"</span>


def main<span style="color:#f92672">(</span>
    host: Host <span style="color:#f92672">=</span> Host.local,
    local: bool <span style="color:#f92672">=</span> False,
    model: ModelChoices <span style="color:#f92672">=</span> ModelChoices.llama31,
    stream: bool <span style="color:#f92672">=</span> False,
<span style="color:#f92672">)</span>:
    <span style="color:#66d9ef">if</span> local:
        host <span style="color:#f92672">=</span> Host.local

    client <span style="color:#f92672">=</span> Client<span style="color:#f92672">(</span>host<span style="color:#f92672">=</span>host.value<span style="color:#f92672">)</span>

    response <span style="color:#f92672">=</span> client.chat<span style="color:#f92672">(</span>
        model<span style="color:#f92672">=</span>model.value,
        messages<span style="color:#f92672">=[</span>
            <span style="color:#f92672">{</span>
                <span style="color:#e6db74">"role"</span>: <span style="color:#e6db74">"user"</span>,
                <span style="color:#e6db74">"content"</span>: <span style="color:#ae81ff">\
</span><span style="color:#ae81ff"></span>                    <span style="color:#e6db74">"Please riff on the 'Llama Llama Red Pajama' book but using AI terms like the 'Ollama' server and the 'Llama 3.1' model."</span>
                    <span style="color:#e6db74">"Instead of using 'Llama Llama', please use 'Ollama Llama 3.1'."</span>,
            <span style="color:#f92672">}</span>
        <span style="color:#f92672">]</span>,
        stream<span style="color:#f92672">=</span>stream,
    <span style="color:#f92672">)</span>

    <span style="color:#66d9ef">if</span> stream:
        <span style="color:#66d9ef">for</span> chunk in response:
            print<span style="color:#f92672">(</span>chunk<span style="color:#f92672">[</span><span style="color:#e6db74">"message"</span><span style="color:#f92672">][</span><span style="color:#e6db74">"content"</span><span style="color:#f92672">]</span>, end<span style="color:#f92672">=</span><span style="color:#e6db74">""</span>, flush<span style="color:#f92672">=</span>True<span style="color:#f92672">)</span>
        print<span style="color:#f92672">()</span>

	<span style="color:#66d9ef">else</span>:
        print<span style="color:#f92672">(</span>f<span style="color:#e6db74">"[yellow]{response['message']['content']}[/yellow]"</span><span style="color:#f92672">)</span>

<span style="color:#66d9ef">if</span> __name__ <span style="color:#f92672">==</span> <span style="color:#e6db74">"__main__"</span>:
    typer.run<span style="color:#f92672">(</span>main<span style="color:#f92672">)</span>

```

</div>Some of my family’s favorite books are the late Anna Dewdney’s [Llama Llama books](https://llamallamabook.com). Please buy and support their work. I can’t read Llama 3.1 and Ollama without considering the “Llama Llama Red Pajama” book.

To set up and run this:

<div class="highlight">```shell
<span style="color:#75715e"># Install a few "nice to have" libraries</span>
➜ pip install ollama rich typer

<span style="color:#75715e"># Run our demo</span>
➜ python hello-llama.py --stream

Here<span style="color:#e6db74">'s a riff on "Llama Llama Red Pajama" but with an AI twist:
</span><span style="color:#e6db74">
</span><span style="color:#e6db74">**Ollama Llama 3.1, Ollama Llama 3.1**
</span><span style="color:#e6db74">Mama said to Ollama Llama 3.1,
</span><span style="color:#e6db74">"Dinner'</span>s <span style="color:#66d9ef">done</span>, time <span style="color:#66d9ef">for</span> some learning fun!<span style="color:#e6db74">"
</span><span style="color:#e6db74">But Ollama Llama 3.1 didn't wanna play
</span><span style="color:#e6db74">With the data sets and algorithms all day.
</span><span style="color:#e6db74">
</span><span style="color:#e6db74">He wanted to go out and get some rest,
</span><span style="color:#e6db74">And dream of neural nets that were truly blessed.
</span><span style="color:#e6db74">But Mama said, "</span>No way, young Ollama Llama 3.1,
You need to train on some more NLP.<span style="color:#e6db74">"
</span><span style="color:#e6db74">
</span><span style="color:#e6db74">Ollama Llama 3.1 got so mad and blue
</span><span style="color:#e6db74">He shouted at the cloud, "</span>I don<span style="color:#e6db74">'t wanna do this too!"
</span><span style="color:#e6db74">But then he remembered all the things he could see,
</span><span style="color:#e6db74">On the Ollama server, where his models would be.
</span><span style="color:#e6db74">
</span><span style="color:#e6db74">So he plugged in his GPU and gave a happy sigh
</span><span style="color:#e6db74">And trained on some texts, till the morning light shone high.
</span><span style="color:#e6db74">He learned about embeddings and wordplay too,
</span><span style="color:#e6db74">And how to chat with humans, that'</span>s what he wanted to <span style="color:#66d9ef">do</span>.

**The end**

```

</div>Connecting to Ollama
--------------------

I have two Macs running Ollama and I use [Tailscale](https://tailscale.com) to bounce between them from anywhere. When I’m at home upstairs it’s quicker to run a local instance. When I’m on my 2019 MacBook Pro it’s faster to connect to the office.

The only stumbling block I ran into was needing to set a few ENV variables setup so that Ollama is listening on a port that I can proxy to. This was frustrating to figure out, but I hope it saves you some time.

<div class="highlight">```shell
➜ launchctl setenv OLLAMA_HOST 0.0.0.0:11434
➜ launchctl setenv OLLAMA_ORIGINS http://*

<span style="color:#75715e"># Restart the Ollama server to pick up on the ENV vars</span>
➜ brew services restart ollama

```

</div>Simon Willison’s LLM tool
-------------------------

I also like using [Simon Willison](https://simonwillison.net)’s [LLM](https://llm.datasette.io/en/stable/) tool, which supports a ton of different AI services via third-party plugins. I like the [llm-ollama](https://pypi.org/project/llm-ollama/) library, which allows us to connect to our local Ollama instance.

When working with Ollama, I start with the Ollama run command, but I have a few bash scripts that might talk to OpenAI or Claude 3.5, and it’s nice to keep my brain in the same tooling space. LLM is useful for mixing and matching remote and local models.

To install and use LLM + llm-ollama + Llama 3.1.

Please note that the Ollama server should already be running as previously outlined.

<div class="highlight">```shell
<span style="color:#75715e"># Install llm</span>
➜ brew install llm

<span style="color:#75715e"># Install llm-ollama</span>
➜ llm install llm-ollama

<span style="color:#75715e"># List all of models from Ollama</span>
➜ llm ollama list-models

<span style="color:#75715e"># </span>
➜ llm -m llama3.1:latest <span style="color:#e6db74">"how much is 2+2?"</span>
The answer to <span style="color:#ae81ff">2</span> + <span style="color:#ae81ff">2</span> is:

<span style="color:#ae81ff">4</span>

```

</div>Bonus: Mistral Large 2
----------------------

While I was working on this post, Mistral AI launched their [Large Enough: Mistral Large 2](https://mistral.ai/news/mistral-large-2407/) model today. The Ollama project released [support for the model](https://ollama.com/library/mistral-large) within minutes of its announcement.

The Mistral Large 2 release is noteworthy because it outperforms Lllama 3.1’s 405B parameter model and is under 1/3 of the size. It is also the second GPT-4 class model release in the last two days.

Check out Simon’s [post](https://simonwillison.net/2024/Jul/24/mistral-large-2/) for more details and another LLM plugin for another way to access it.

Originally posted on: https://micro.webology.dev/2024/07/24/ollama-llama-red.html