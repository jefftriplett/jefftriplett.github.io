---
category: micro.blog
date: '2024-04-19T04:41:03.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: super-bot-fight
title: 🤖 Super Bot Fight 🥊
redirect_to: https://micro.webology.dev/2024/04/18/super-bot-fight/
tags:
- Django
- Python
---

In March, I wrote about my robots.txt research and how I started proactively and defensively blocking AI Agents in my [🤖 On Robots.txt](https://micro.webology.dev/2024/03/20/on-robotstxt.html). Since March, I have updated my Django projects to add more robots.txt rules.

Earlier this week, I ran across this [Blockin’ bots.](https://ethanmarcotte.com/wrote/blockin-bots/) blog post and this example, the `mod_rewrite` rule blocks AI Agents via their User-Agent strings.

```
<IfModule mod_rewrite.c>
RewriteEngine on
RewriteBase /
# block “AI” bots
RewriteCond %{HTTP_USER_AGENT} (AdsBot-Google|Amazonbot|anthropic-ai|Applebot|AwarioRssBot|AwarioSmartBot|Bytespider|CCBot|ChatGPT|ChatGPT-User|Claude-Web|ClaudeBot|cohere-ai|DataForSeoBot|Diffbot|FacebookBot|FacebookBot|Google-Extended|GPTBot|ImagesiftBot|magpie-crawler|omgili|Omgilibot|peer39_crawler|PerplexityBot|YouBot) [NC]
RewriteRule ^ – [F]
</IfModule>
```

Since none of my projects use Apache, and I was short on time, I decided to leave this war to the bots.

## Django Middleware

I asked ChatGPT to convert this snippet to a piece of Django Middleware called Super Bot Fight. After all, if we don’t have time to keep up with bots, then we could leverage this technology to help fight against them.

In theory, this snippet passed my eyeball test and was good enough:

```
# middleware.py

from django.http import HttpResponseForbidden

# List of user agents to block

BLOCKED_USER_AGENTS = [
    "AdsBot-Google",
    "Amazonbot",
    "anthropic-ai",
    "Applebot",
    "AwarioRssBot",
    "AwarioSmartBot",
    "Bytespider",
    "CCBot",
    "ChatGPT",
    "ChatGPT-User",
    "Claude-Web",
    "ClaudeBot",
    "cohere-ai",
    "DataForSeoBot",
    "Diffbot",
    "FacebookBot",
    "Google-Extended",
    "GPTBot",
    "ImagesiftBot",
    "magpie-crawler",
    "omgili",
    "Omgilibot",
    "peer39_crawler",
    "PerplexityBot",
    "YouBot",
]

class BlockBotsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check the User-Agent against the blocked list
        user_agent = request.META.get("HTTP_USER_AGENT", "")
        if any(bot in user_agent for bot in BLOCKED_USER_AGENTS):
            return HttpResponseForbidden("Access denied")
        response = self.get_response(request)
        return response
```

To use this middleware, you would update your Django `settings.py` to add it to your `MIDDLEWARE` setting.

```
# settings.py

MIDDLEWARE = [
    ...
    "middleware.BlockBotsMiddleware",
    ...
]
```

## Tests?

If this middleware works for you and you care about testing, then these tests should also work:

```
import pytest

from django.http import HttpRequest
from django.test import RequestFactory

from middleware import BlockBotsMiddleware

@pytest.mark.parametrize("user_agent, should_block", [
    ("AdsBot-Google", True),
    ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", False),
    ("ChatGPT-User", True),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3", False),
])
def test_user_agent_blocking(user_agent, should_block):
    # Create a request factory to generate request instances
    factory = RequestFactory()
    request = factory.get('/', HTTP_USER_AGENT=user_agent)

    # Middleware setup
    middleware = BlockBotsMiddleware(get_response=lambda request: HttpResponse())
    response = middleware(request)

    # Check if the response should be blocked or allowed
    if should_block:
        assert response.status_code == 403, f"Request with user agent '{user_agent}' should be blocked."
    else:
        assert response.status_code != 403, f"Request with user agent '{user_agent}' should not be blocked."
```

## Enhancements

To use this code in production, I would normalize the `user_agent` and `BLOCKED_USER_AGENTS` variables to be case-insensitive.

I would also consider storing my list of user agents in a Django model or using a project like [django-robots](https://github.com/jazzband/django-robots) instead of a hard-coded Python list.
