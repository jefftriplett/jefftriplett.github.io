---
category: micro.blog
date: 2025-01-11T16:22:36.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: django-templated-email-md-notes-aka-if-you-want-to-format-emails-with-markdown-use-it
title: "django-templated-email-md notes aka if you want to format emails with Markdown, use it"
redirect_to: https://micro.webology.dev/2025/01/11/djangotemplatedemailmd-notes-aka-if-you/
tags:
---

I launched [Django News Jobs](https://jobs.django-news.com) two DjangoCon USs ago, and I somehow put off deploying emails until this week. So, every day or two, I check my Review Jobs queue to see if there’s anything new to approve or reject.

✅ Sending emails with Django is straightforward and not very painful.

🤔 Working with most email providers and troubleshooting issues is painful.

🤔 Starting with a blank page and styling emails is painful.

I tried a few third-party apps that I fought with before landing on [Jack Linke](https://jacklinke.com)’s [django-templated-email-md](https://github.com/OmenApps/django-templated-email-md) (DTEM), which just worked. DTEM doesn’t re-invent the wheel, but it does let me write my email messages with Markdown, which turns out to be all I need.

To add email support, I followed the [Usage Guide](https://django-templated-email-md.readthedocs.io/en/latest/usage.html) and then I added one send email function per email that I wanted to send. I’ll eventually refactor this, but it was good enough to get started.

`jobs/models.py`
----------------

For the curious, the code looks like:

<div class="highlight">```python
<span style="color:#75715e"># jobs/models.py</span>

<span style="color:#75715e"># a bunch of imports ... </span>

<span style="color:#f92672">from</span> templated_email <span style="color:#f92672">import</span> send_templated_mail

<span style="color:#f92672">...</span>

<span style="color:#66d9ef">class</span> <span style="color:#a6e22e">Job</span>(models<span style="color:#f92672">.</span>Model):
    <span style="color:#f92672">...</span>

    <span style="color:#66d9ef">def</span> <span style="color:#a6e22e">send_job_new_email</span>(self):
        send_templated_mail(
            template_name<span style="color:#f92672">=</span><span style="color:#e6db74">"job_new"</span>,
            from_email<span style="color:#f92672">=</span>settings<span style="color:#f92672">.</span>DEFAULT_FROM_EMAIL,
            recipient_list<span style="color:#f92672">=</span>settings<span style="color:#f92672">.</span>ADMINS,
            context<span style="color:#f92672">=</span>{
                <span style="color:#e6db74">"job"</span>: self,
            },
        )

```

</div>`send_templated_mail` does the actual sending, and `template_name` will look for a template file called `job_new.md`, which will contain our Markdown message.

You can put anything you want in `context`, but I will include the `job` so we can include as many details from our job submission as possible.

To send a Job, I can call `job.send_job_new_email()` via a signal, cron job, or after someone submits a Job for approval.

`templates/emails/job_new.md`
-----------------------------

My emails contain both a “subject” and “content” block, and DTEM figures out the rest for me.

<div class="highlight">```html
<span style="color:#75715e"><!-- templates/emails/job_new.md --></span>

{% block subject %}[{{ site_name }}] New Job Posting: {{ job.title }} at {{ job.employer_name }}{% endblock %}

{% block content %}
# New Job Listing Posted

A new job has been posted on the website:

- **Title:** {{ job.title }}
- **Company:** {{ job.employer_name }}
- **Location:** {{ job.location }}
- **Remote:** {{ job.get_remote_display }}

You can view the full job listing here: <<span style="color:#f92672">a</span> <span style="color:#a6e22e">href</span><span style="color:#f92672">=</span><span style="color:#e6db74">"{{ job.get_absolute_url_with_domain }}"</span>>{{ job.get_absolute_url_with_domain }}</<span style="color:#f92672">a</span>>
{% endblock content %}

```

</div>My `get_absolute_url_with_domain` calls in my templates are my workaround for Django’s existential crisis of not making it easy to include the domain name in my urls.

Bonus: Django-Q2
----------------

I paired DTEM with [Django-Q2](https://github.com/django-q2/django-q2), my favorite Django task queue. It can work with just the Django ORM, which is good enough for projects like Django News Jobs, which are relatively low traffic but spiky traffic.

If my email-sending provider times out or I have an issue, like my credit card expiring, I never want a user to see it. So, I use a task queue to handle all potentially blocking processes, like sending emails.

Django-Q2 is painless to configure. Using it involves importing `async_task` and modifying our `send_templated_mail` method to be an argument to the `async_task` method.

<div class="highlight">```python
<span style="color:#75715e"># jobs/models.py</span>

<span style="color:#75715e"># a bunch of imports ... </span>

<span style="color:#f92672">from</span> django_q.tasks <span style="color:#f92672">import</span> async_task
<span style="color:#f92672">from</span> templated_email <span style="color:#f92672">import</span> send_templated_mail

<span style="color:#f92672">...</span>

<span style="color:#66d9ef">class</span> <span style="color:#a6e22e">Job</span>(models<span style="color:#f92672">.</span>Model):
    <span style="color:#f92672">...</span>

    <span style="color:#66d9ef">def</span> <span style="color:#a6e22e">send_job_new_email</span>(self):
        async_task(
            send_templated_mail,
            template_name<span style="color:#f92672">=</span><span style="color:#e6db74">"job_new"</span>,
            from_email<span style="color:#f92672">=</span>settings<span style="color:#f92672">.</span>DEFAULT_FROM_EMAIL,
            recipient_list<span style="color:#f92672">=</span>settings<span style="color:#f92672">.</span>ADMINS,
            context<span style="color:#f92672">=</span>{
                <span style="color:#e6db74">"job"</span>: self,
            },
        )

```

</div>If a Job was sent successfully, I can now check the Django Admin to see if there were any failures.

Forward Email
-------------

Now that we have an email confirmed to send, my go-to provider for side projects is [Forward Email](https://forwardemail.net). They allow outbound SMTP and even support webhooks, which I might write about some other time.

I like them over Mailchimp, Sendmail, and Gmail because they are cheap ($3 a month) and let me have unlimited domains and aliases. I have used them for a dozen side projects for several years now, and they just work. I gave up on Sendmail because I spent more time fighting with them to not turn off my account because the volume was too low. It’s worth $36 a year to have to fight this fight again.

Forward Email’s products and services are fully open-source if you care about such things.

Originally posted on: https://micro.webology.dev/2025/01/11/djangotemplatedemailmd-notes-aka-if-you/
