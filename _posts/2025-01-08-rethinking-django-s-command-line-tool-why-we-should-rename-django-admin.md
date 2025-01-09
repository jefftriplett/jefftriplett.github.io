---
category: micro.blog
date: 2025-01-09T01:15:02.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: rethinking-django-s-command-line-tool-why-we-should-rename-django-admin
title: "🤔 Rethinking Django's Command-Line Tool: Why We Should Rename `django-admin`"
redirect_to: https://micro.webology.dev/2025/01/08/rethinking-djangos-commandline-tool-why/
tags: 
---

Django has been a key tool for Python web developers for many years. But as new frameworks like FastAPI become prevalent, it’s important to ensure Django stays easy for new and experienced developers. Recently, a [discussion thread](https://forum.djangoproject.com/t/name-the-main-command-django/37230) received over 60 comments about changing Django’s main command from `django-admin` to something else, like `django`. The thread also explored other `django-cmd` possibilities, showcasing many ideas. While the conversation was broad, I want to focus on why renaming `django-admin` is a good idea.

Why Rename `django-admin`?
--------------------------

### Keep It Simple and Pythonic

When I chaired DjangoCon US, a common question I asked attendees during our opening session was whether they learned Django first or Python first. It surprised me to see the majority of hands raised for “Django first,” which meant that learning Django taught them Python. This showed me how important Django is for teaching Python.

Because Django helps so many people learn Python, it should follow Python’s simple and clean style. Changing `django-admin` to `django` makes the command easier to remember and use. New developers won’t have to remember an extra non-off command, making their experience smoother.

### Easy Transition for Everyone

One great thing about `django-admin` is that it has been the same for many years. If we rename it to `django`, we don’t have to remove `django-admin`. Instead, we can make `django` an alias for `django-admin`. This way, old projects can keep using `django-admin`, and new projects can use `django`. This change won’t disrupt anyone’s work.

Real-Life Benefits
------------------

This change is prompted by common problems in the Django community. For example, a [forum post](https://forum.djangoproject.com/t/running-django-admin-as-a-python-module/36401) showed that some developers get confused when trying to run `django-admin` as a Python module. They saw errors like `ModuleNotFound` because it wasn’t obvious why `python -m django-admin` didn’t work.

### Improving Compatibility with Tools Like UV

Another issue is that commands like `uv tool run django` don’t work as expected, but they could. Python’s best practices support using `python -m django`, which would work smoothly with tools like UV if Django updated its command structure. Instead, the “correct” answer is to run `uv tool run --from django django-admin` to bootstrap a Django project.

Renaming `django-admin` to `django` and aligning with Python’s module execution standards can make integrating Django with such tools just work. This change would help developers avoid errors and follow best practices, enhancing overall compatibility and workflow.

As it exists today, a new user has to learn to use `django-admin` to start a project, and then later, once they learn from seeing `python -m pip` used.

Balancing Old and New
---------------------

Django has been around for a long time and has a strong history. It’s important to keep what makes Django great while also making improvements. Renaming `django-admin` to `django` respects Django’s past and helps it move forward. This change keeps Django reliable for long-time users while improving it for new developers.

Is this change zero work?
-------------------------

No, it requires a [one-line config change](https://micro.webology.dev/2024/12/14/new-project-to-shorten-djangoadmin/) and replacing every instance of `django-admin` in the docs. Any changes in Django’s docs will inevitably trigger translation changes, but these should be small and tightly scoped. As of today, there are [39-page instances](https://docs.djangoproject.com/en/5.1/search/?q=%22django-admin%22) to update.

Conclusion
----------

Renaming `django-admin` to `django` improves Django’s developer experience. This new name makes the command more straightforward to remember and follows Python’s best practices. It also makes it simpler for new developers to start with modern tools like UV.

Although this change means updating some configuration files and documentation, the long-term benefits of having a clearer and more Python-like command are much greater than the initial work needed. Keeping `django-admin` as an alias also ensures that existing projects continue to work without problems.

---

Join the conversation [here](https://forum.djangoproject.com/t/name-the-main-command-django/37230) and share your ideas on making Django even better for everyone.

PS: This piece was written quickly and proofed even more quickly with Grammarly.

Originally posted on: https://micro.webology.dev/2025/01/08/rethinking-djangos-commandline-tool-why/