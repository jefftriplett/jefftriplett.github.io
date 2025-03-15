---
category: micro.blog
date: 2024-10-05T17:43:54.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: uv-with-github-actions-to-run-an-rss-to-readme-project
title: "UV with GitHub Actions to run an RSS to README project"
redirect_to: https://micro.webology.dev/2024/10/05/uv-with-github.html
tags:
---

2024-10-05 UV with GitHub Actions to run an RSS to README project
=================================================================

For my personal [GitHub profile](https://github.com/jefftriplett/jefftriplett), I list my activities, affiliations, and the latest updates from some of my projects.

Historically, I have used [JasonEtco/rss-to-readme](https://github.com/JasonEtco/rss-to-readme) GitHub Action to fetch a few RSS feeds or two and to update my README a few times a day.

Overall, I’m happy with this setup. I used it on the Django News GitHub Organization to pull in newsletter issues, jobs, and the latest videos from our various projects. When I tried to install rss-to-readme in our repo, I was getting node12 errors. (Have I mentioned how much I loathe node/npm?).

Instead of forking rss-to-readme and trying to figure out how to upgrade it, I used this as an excuse to “pair program” with [Claude](https://claude.ai). We quickly built out a prototype using Python and the [feedparser](https://github.com/kurtmckee/feedparser) library.

I would share the chat log, but it’s mostly me trying out a few different ways to invoke it before I settle on the finished approach. See the source code over on GitHub if you are curious: <https://github.com/django-news/.github/blob/main/fetch-rss.py>

Once I had a working Python script that could fetch an RSS file and modify the README, I decided to run/deploy it using [UV](https://github.com/astral-sh/uv) to see how minimal I could build out the GitHub Action.

GitHub Action
-------------

To run our `fetch-rss.py` script, we have four steps:

1. `actions/checkout` Get a git checkout of our project.
2. `astral-sh/setup-uv` Setup UV also installs Pythons for us. As a bonus, we enabled UV’s cache support, which will run much faster in the future unless we change something in our fetch-rss.py file.
3. Run `uv run fetch-rss.py ...` to fetch our RSS feeds and write them to disk. `uv run` installs any dependencies and caches them before our `fetch-rss.py` runs.
4. `stefanzweifel/git-auto-commit-action` If our README.md file has changed, save our changes and commit them back to git and into our README.

Our `schedule.yml` GitHub Action workflow runs twice daily or whenever we push a new change to our repo. We also set `workflow_dispatch,` which gives us a button to run the script manually.

<div class="highlight">```yaml
<span style="color:#75715e"># .github/workflows/schedule.yml</span>
<span style="color:#f92672">name</span>: <span style="color:#ae81ff">Update README</span>


<span style="color:#f92672">on</span>:
  <span style="color:#f92672">push</span>:
    <span style="color:#f92672">branches</span>:
      - <span style="color:#ae81ff">main</span>
  <span style="color:#f92672">schedule</span>:
    <span style="color:#75715e"># Once a day at 12 AM</span>
    - <span style="color:#f92672">cron</span>: <span style="color:#ae81ff">0</span> <span style="color:#ae81ff">12</span> * * *
  <span style="color:#f92672">workflow_dispatch</span>:


<span style="color:#f92672">jobs</span>:
  <span style="color:#f92672">update</span>:
    <span style="color:#f92672">runs-on</span>: <span style="color:#ae81ff">ubuntu-latest</span>


    <span style="color:#f92672">permissions</span>:
      <span style="color:#f92672">contents</span>: <span style="color:#ae81ff">write</span>


    <span style="color:#f92672">steps</span>:
      - <span style="color:#f92672">uses</span>: <span style="color:#ae81ff">actions/checkout@v4</span>


      - <span style="color:#f92672">name</span>: <span style="color:#ae81ff">Install uv</span>
        <span style="color:#f92672">uses</span>: <span style="color:#ae81ff">astral-sh/setup-uv@v3</span>
        <span style="color:#f92672">with</span>:
          <span style="color:#f92672">enable-cache</span>: <span style="color:#66d9ef">true</span>
          <span style="color:#f92672">cache-dependency-glob</span>: |<span style="color:#e6db74">
</span><span style="color:#e6db74">            </span>            <span style="color:#75715e">*.py</span>


      - <span style="color:#f92672">name</span>: <span style="color:#ae81ff">Fetch our Feeds</span>
        <span style="color:#f92672">run</span>: |<span style="color:#e6db74">
</span><span style="color:#e6db74">          # Fetch latest Django News Newsletter entries
</span><span style="color:#e6db74">          uv run fetch-rss.py \
</span><span style="color:#e6db74">              --section=news \
</span><span style="color:#e6db74">              --readme-path=profile/README.md \
</span><span style="color:#e6db74">              https://django-news.com/issues.rss</span>  


      - <span style="color:#f92672">uses</span>: <span style="color:#ae81ff">stefanzweifel/git-auto-commit-action@v5</span>
        <span style="color:#f92672">with</span>:
          <span style="color:#f92672">commit_message</span>: <span style="color:#e6db74">":pencil: Updates README"</span>

```

</div>Results
-------

Overall, I’m pleased with this solution. If I wanted to spend more time on it or re-use this workflow, I might turn it into a GitHub Action workflow so that we can call: `django-news/rss-to-readme` to use in other projects. For now, this is fine.

I’m happy with the `astral-sh/setup-uv` and `uv run` steps because they save me from having to set up Python and then install our project dependencies as separate steps.

I normally shy away from running Python workflows like this in GitHub Actions because they involve a lot of slow steps. This entire workflow takes 16 to 20 seconds to run, which feels fast to me.

Originally posted on: https://micro.webology.dev/2024/10/05/uv-with-github.html
