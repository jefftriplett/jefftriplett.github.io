# :snippet snippet-example-05

from model_bakery import baker

from news.serializers import CategorySerializer


def test_category_post(tp):
    # Create a Category fixture
    obj = baker.prepare("news.Category")

    # Use a DRF ModelSerializer to give us JSON
    payload = CategorySerializer(obj).data

    # Use a reverse lookup to find our endpoint's url
    url = tp.reverse("category-detail")

    # Login as a valid test user
    tp.client.login()

    # Send our test payload to our endpoint
    response = tp.client.post(url, payload, content_type="application/json")

    # Was our request valid?
    tp.response_200(response)

# :endsnippet
