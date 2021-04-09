---
category: Python
date: 2017-06-16 14:24:00 -0600
image: https://generator.opengraphimg.com/?atSymbol=true&author=webology&authorSize=text-2xl&tags=python&title=Pathlib+Is+Wonderful%21
layout: post
location: Lawrence, Kansas United States
tags:
- python
title: Pathlib Is Wonderful!
weather: 82˚F - It was partly cloudy.
---

[pathlib][] is a wonderful addition to the Python 3 standard library. The library is an "Object-oriented filesystem paths" module which combines the best of Python's file system modules like `os`, `os.path`, and `glob` to name a few. This simplifies the number of modules you'll have to import to work with files and folders. 

Here are some highlights that I have noticed in just a few days of playing with the pathlib.

## Working with folders

```python
>>> from pathlib import Path

>>> Path('docs').exists()
False

>>> Path('docs').mkdir()

>>> Path('docs').is_dir()
True
```

### Listing all of the files in a folder

```python
>>> Path('docs').glob('*.md')
<generator object Path.glob at 0x1128ee258>

# Since generator output isn't obvious :)
>>> [item for item in Path('docs').glob('*.md')]
[PosixPath('docs/README.md')]
```

## Working with files

```python
>>> Path('docs', 'README.md').is_file()
True

>>> Path('docs').joinpath('README.md')
```

### Opening a file

```python
>>> Path('README.md').open('r').read()
```

### Writing to a file

```python
>>> Path('README.md').write_text('Read the Docs!')
```

### Reading from file

```python
>>> Path('README.md').read_text()
'Read the Docs!'
```

### What about Python 2?

Even though pathlib is built into Python 3, there is a [Python 2.7 backport](https://github.com/mcmtroffaes/pathlib2) for anyone who can't switch yet.

Thank you [George Hickman](https://twitter.com/ghickman) for pointing this out to me on Twitter!

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">There’s even a backport for py2!</p>&mdash; George Hickman (@ghickman) <a href="https://twitter.com/ghickman/status/875256380567015424">June 15, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

[pathlib]: https://docs.python.org/3/library/pathlib.html