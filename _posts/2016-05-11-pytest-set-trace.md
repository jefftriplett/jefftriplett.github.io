---
category: TIL
date: 2016-05-11
image: https://generator.opengraphimg.com/?atSymbol=true&author=webology&authorSize=text-2xl&style=modern&tags=python%2Cpytest%2Cpy.test%2Cpdb&title=Use+%60pytest.set_trace%60+to+set+a+breakpoint+in+py.test
layout: post
location: Lawrence, Kansas United States
tags:
- python
- pytest
- py.test
- pdb
title: Use `pytest.set_trace` to set a breakpoint in py.test
---

To set a breakpoint in py.test, use:

```python
import pytest

pytest.set_trace()
```

[source](https://docs.pytest.org/en/latest/usage.html?highlight=breakpoint#setting-a-breakpoint-aka-set-trace)
