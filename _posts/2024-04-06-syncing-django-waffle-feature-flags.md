---
category: micro.blog
date: '2024-04-06T02:58:28.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: syncing-django-waffle-feature-flags
title: ⛳ Syncing Django Waffle feature flags
redirect_to: https://micro.webology.dev/2024/04/05/syncing-django-waffle-feature-flags/
tags:
- Django
- Python
---

The [django-waffle](https://github.com/jazzband/django-waffle) feature flag library is helpful for projects where we want to release and test new features in production and have a controlled rollout. I also like using feature flags for resource-intensive features on a website that we want to toggle off during high-traffic periods. It’s a nice escape hatch to fall back on if we need to turn off a feature and roll out a fix without taking down your website.

While Waffle is a powerful tool, I understand the challenge of keeping track of feature flags in both code and the database. It’s a pain point that many of us have experienced.

Waffle has a `WAFFLE_CREATE_MISSING_FLAGS=True` setting that we can use to tell Waffle to create any missing flags in the database should it find one. While this helps discover which flags our application is using, we need to figure out how to clean up old flags in the long term.

The pattern I landed on combines storing all our known feature flags and a note about what they do in our main settings file.

```
# settings.py
... 

WAFFLE_CREATE_MISSING_FLAGS=True

WAFFLE_FEATURE_FLAGS = {
   "flag_one": "This is a note about flag_one",
   "flag_two": "This is a note about flag_two",
}
```

We will use a management command to sync every feature flag we have listed in our settings file, and then we will clean up any missing feature flags.

```
# management/commands/sync_feature_flags.py
import djclick as click

from django.conf import settings
from waffle.models import Flag


@click()
def command():
    # Create flags that don't exist
    for name, note in settings.WAFFLE_FEATURE_FLAGS.items():
        flag, created = Flag.objects.update_or_create(
            name=name, defaults={"note": note}
        )
        if created:
            print(f"Created flag {name} ({flag.pk})")

    # Delete flags that are no longer registered in settings
    for flag in Flag.objects.exclude(name__in=settings.FEATURE_FLAGS.keys()):
        flag.delete()
        print(f"Deleted flag {flag.name} ({flag.pk})")
```

We can use the `WAFFLE_CREATE_MISSING_FLAGS` settings as a failsafe to create any flags we might have accidently missed. They will stick out because they will not have a note associated with them.

This pattern is also helpful in solving similar problems for scheduled tasks, which might also store their schedules in the database.

Check out this example in the [Django Styleguide](https://github.com/HackSoftware/Django-Styleguide?tab=readme-ov-file#periodic-tasks) for how to sync Celery’s scheduled tasks.
