---
category: micro.blog
date: '2024-02-24T20:21:43.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: fetch-the-contents-of-a-url-with-django-service
title: Fetch the contents of a URL with Django service
redirect_to: https://micro.webology.dev/2024/02/24/fetch-the-contents-of-a/
tags:
- Django
- Python
---

For the last few months, I have been using the [cooked.wiki](https://cooked.wiki) recipe-saving website, which initially impressed me because of how easy the website’s API is to use.

To use the service, all one has to do is prepend any website that contains a food recipe with `https://cooked.wiki/`, and you get the recipe without a coming-of-age discovery story.

This is a fun pattern, so I wrote my own in Django to illustrate how to build a Django view, which accepts a URL like http://localhost:8000/https://httpbin.org/get/ where <https://httpbin.org/get/> will be fetched and the contents stored for processing.

```
# views.py 
import httpx

from django.http import HttpResponse
from urllib.parse import urlparse

def fetch_content_view(request, url: str) -> HttpResponse:
    # Ensure the URL starts with http:// or https://
    parsed_url = urlparse(url)
    if parsed_url.scheme in ("http", "https"):
        try:
            response = httpx.get(url)

            # Check for HTTP request errors
            httpx.raise_for_status()
            content = httpx.content

            # TODO: do something with content here...
            assert content
            return HttpResponse(f"{url=}")

        except httpx.RequestException as e:
            return HttpResponse(f"Error fetching the requested URL: {e}", status=500)

    else:
        return HttpResponse("Invalid URL format.", status=400)
```

```
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # other URL patterns here...
    ...
    
    path("<path:url>/", views.fetch_content_view, name="fetch_content"),
]
```

If you create your fetch the contents of a URL-like service, please consider putting it behind authentication to avoid someone discovering it and using it to DDOS someone’s website. I recommend throttling the view to prevent overloading a website by spamming requests to it.

**Updated:** I updated the example to switch from the python-requests references to the [HTTPX](https://www.python-httpx.org/compatibility/) library.
