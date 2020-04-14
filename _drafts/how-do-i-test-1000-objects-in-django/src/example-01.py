from model_bakery import baker

category = baker.make("news.Category")

assert category.name
