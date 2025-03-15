---
category: micro.blog
date: 2024-07-13T14:31:37.000000Z
layout: post
location: Home @ Lawrence, Kansas United States
slug: duckdb-may-be-the-tool-you-didn-t-know-you-were-missing
title: "🦆 DuckDB may be the tool you didn't know you were missing"
redirect_to: https://micro.webology.dev/2024/07/12/duckdb-may-be.html
tags:
---

🤔 I haven’t fully figured out [DuckDB](https://duckdb.org) yet, but it’s worth trying out if you are a Python dev who likes to work on data projects or gets frequently tasked with data import projects.

DuckDB is a fast database engine that lets you read CSV, Parquet, and JSON files and query them using SQL. Instead of importing data into your database, DuckDB enables you to write SQL and run it against these file types.

I have a YouTube to frontmatter project that can read a YouTube playlist and write out each video to a markdown file. I modified the export script to save the raw JSON output to disk.

I used DuckDB to read a bunch of JSON files using the following script:

<div class="highlight">```python
<span style="color:#f92672">import</span> duckdb

<span style="color:#66d9ef">def</span> <span style="color:#a6e22e">main</span>():
    result <span style="color:#f92672">=</span> duckdb<span style="color:#f92672">.</span>sql(<span style="color:#e6db74">"SELECT id,snippet FROM read_json('data/*.json')"</span>)<span style="color:#f92672">.</span>fetchall()

    <span style="color:#66d9ef">for</span> row <span style="color:#f92672">in</span> result:
        id, snippet <span style="color:#f92672">=</span> row
        print(<span style="color:#e6db74">f</span><span style="color:#e6db74">"</span><span style="color:#e6db74">{</span>id<span style="color:#e6db74">=}</span><span style="color:#e6db74">"</span>)
        print(snippet[<span style="color:#e6db74">"channelTitle"</span>])
        print(snippet[<span style="color:#e6db74">"title"</span>])
        print(snippet[<span style="color:#e6db74">"publishedAt"</span>])
        print(snippet[<span style="color:#e6db74">"description"</span>])
        print()


<span style="color:#66d9ef">if</span> __name__ <span style="color:#f92672">==</span> <span style="color:#e6db74">"__main__"</span>:
    main()

```

</div>This script accomplishes several things:

- It reads over 650 JSON files in about one second.
- It uses SQL to query the JSON data directly.
- It extracts specific fields (id and snippet) from each JSON file.

Performance and Ease of Use
---------------------------

The speed at which DuckDB processes these files is remarkable. In traditional setups, reading and parsing this many JSON files could take significantly longer and require more complex code.

When to Use DuckDB
------------------

DuckDB shines in scenarios where you need to:

- Quickly analyze data in files without a formal import process.
- Perform SQL queries on semi-structured data (like JSON)
- Process large datasets efficiently on a single machine.

Conclusion
----------

DuckDB is worth trying out in your data projects. If you have a lot of data and you need help with what to do with it, being able to write SQL against hundreds of files is powerful and flexible.

Originally posted on: https://micro.webology.dev/2024/07/12/duckdb-may-be.html
