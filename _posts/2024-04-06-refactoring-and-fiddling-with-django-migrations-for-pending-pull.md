---
category: micro.blog
date: '2024-04-06T19:59:54.000000Z'
layout: post
location: Home @ Lawrence, Kansas United States
slug: refactoring-and-fiddling-with-django-migrations-for-pending-pull
title: 🚜 Refactoring and fiddling with Django migrations for pending pull requests 🐘
redirect_to: https://micro.webology.dev/2024/04/06/refactoring-and-fiddling-with-django/
tags:
- Django
- Python
---

One of Django’s most powerful features is the ORM, which includes a robust migration framework. One of Django’s most misunderstood features is Django migrations because it just works 99% of the time.

Even when working solo, Django migrations are highly reliable, working 99.9% of the time and offering better uptime than most web services you may have used last week.

The most common stumbling block for developers of all skill levels is rolling back a Django migration and prepping a pull request for review.

I’m not picky about pull requests or git commit history because I default to using the “Squash and merge” feature to turn all pull request commits into one merge commit. The merge commit tells me when, what, and why something changed if I need extra context.

I am pickier about seeing >2 database migrations for any app unless a data migration is involved. It’s common to see 4 to 20 migrations when someone works on a database feature for a week. Most of the changes tend to be fiddly, where someone adds a field, renames the field, renames it again, and then starts using it, which prompts another `null=True` change followed by a `blank=True` migration.

For small databases, none of this matters.

For a database with 10s or 100s of millions of records, these small changes can cause minutes of downtime *per* migration, which amounts to a throwaway change. While there are ways to mitigate most migration downtime situations, that’s different from my point today.

I’m also guilty of being fiddly with my Django model changes because I know I can delete and refactor them before requesting approval. The process I use is probably worth sharing because once every new client comes up.

Let’s assume I am working on [Django News Jobs](https://jobs.django-news.com), and I am looking over my pull request one last time before I ask someone to review it. That’s when I noticed four migrations that could quickly be rebuilt into one, starting with my `0020*` migration in my `jobs` app.

The rough steps that I would do are:

```
# step 1: see the state of our migrations
$ python -m manage showmigrations jobs
jobs
 [X] 0001_initial
 ...
 [X] 0019_alter_iowa_versus_unconn
 [X] 0020_alter_something_i_should_delete
 [X] 0021_alter_uconn_didnt_foul
 [X] 0022_alter_nevermind_uconn_cant_rebound
 [X] 0023_alter_iowa_beats_uconn
 [X] 0024_alter_south_carolina_sunday_by_four

# step 2: rollback migrations to our last "good" state
$ python -m manage migrate jobs 0019

# step 3: delete our new migrations
$ rm jobs/migrations/002*

# step 4: rebuild migrations 
python -m manage makemigrations jobs 

# step 5: profit 
python -m manage migrate jobs
```

95% of the time, this is all I ever need to do.

Occasionally, I check out another branch with conflicting migrations, and I’ll get my **local** database in a weird state.

In those cases, check out the `--fake` (“Mark migrations as run without actually running them.") and `--prune` (“Delete nonexistent migrations from the `django_migrations` table.") options. The fake and prune operations saved me several times when my `django_migrations` table was out of sync, and I knew that SQL tables were already altered.

## What not `squashmigrations`?

Excellent question. [Squashing migrations](https://docs.djangoproject.com/en/5.0/topics/migrations/#migration-squashing) is wonderful if you care about keeping every or most of the operations each migration is doing. Most of the time, I do not, so I overlook it.
