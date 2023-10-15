import json
from django.http import JsonResponse
from django.http import HttpRequest
from products.models import Product

# json.loads(s) -> Deserialize ``s`` (a ``str``, ``bytes`` or ``bytearray`` instance containing a JSON document) to a Python object.

# request -> It is an instance of HttpRequest -> Django # Nothing to do with python requests
# request.body gives byte string JSON data
# request.GET gives the URL query parameters
# request.headers gives the request headers of the HttpRequest object
# request.content_type directly gives the content type of the HttpRequest 

""" def api_home(request: HttpRequest, *args, **kwargs):
    body = request.body
    params = request.GET
    data = {}
    try:
        data['body'] = json.loads(body)
        data['params'] = dict(params)
    except:
        pass
    print(data.keys())
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data) """

def api_home(request: HttpRequest, *args, **kwargs):
    params = dict(request.GET)
    print(params['title'])
    products = Product.objects.all().order_by("?")
    print(products)
    data = {}
    for product in products:
        if product.title == params['title'][0]:
            data['id'] = product.id
            data['title'] = product.title
            data['content'] = product.content
            data['price'] = str(product.price)
    print(data.keys())
    return JsonResponse(data)