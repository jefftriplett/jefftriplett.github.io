<!-- snippet-example-01-->

```python
from model_bakery import baker

category = baker.make("news.Category")

assert category.name
```
