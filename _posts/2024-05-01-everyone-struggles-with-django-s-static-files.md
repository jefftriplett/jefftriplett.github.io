---
category: micro.blog
date: '2024-05-01T03:07:44.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: everyone-struggles-with-django-s-static-files
title: 🎒 Everyone struggles with Django's static files
redirect_to: https://micro.webology.dev/2024/04/30/everyone-struggles-with-djangos-static/
tags:
- Django
- Python
---

Josh Thomas did a great job documenting and walking us through how he prefers to set up static files in his Django projects last week in his [How I organize `staticfiles` in my Django projects](https://joshthomas.dev/blog/2024/how-i-organize-staticfiles-in-my-django-projects/) article.

Josh recommends the following config and naming convention:

```
# settings.py

# django.contrib.staticfiles
STATIC_ROOT = BASE_DIR / "staticfiles"

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static" / "dist",
    BASE_DIR / "static" / "public",
]
```

Overall, this is very similar to what I do, but I settled into calling my `STATICFILES_DIRS` folder `assets` or `frontend`. After seeing Josh’s example, I changed this value to `staticfiles` to match the setting variable more closely.

## Updated config

```
# settings.py

# django.contrib.staticfiles

# INPUT: Where to look for static files
STATICFILES_DIRS = [
    BASE_DIR / "staticfiles" / "dist",
    BASE_DIR / "staticfiles" / "public",
]

# OUTPUT: Where to put and look for static files to serve
STATIC_ROOT = BASE_DIR / "static"

# SERVE: Where to serve static files
STATIC_URL = "/static/"
```

This also changes our `.gitignore` to match our new settings. Since all of our files will be collected by Django and placed into the `static` folder, we can tell git to ignore this folder.

We can also ignore the `staticfiles/dist/` folder if we have an asset building pipeline and need a place to store the intermediate files.

```
#.gitignore
static/
staticfiles/dist/
# Optionally, to universally ignore all 'dist' directories:
# dist
```
