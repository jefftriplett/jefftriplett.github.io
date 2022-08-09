<!-- Snippet snippet-example-02 -->
```python
from model_bakery import baker

categories = baker.make("news.Category", _quantity=1000)

assert len(categories) == 1000
```
