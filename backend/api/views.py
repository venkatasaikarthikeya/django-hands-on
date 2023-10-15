import json
from django.http import JsonResponse, HttpResponse
from django.http import HttpRequest
from products.models import Product
from django.forms.models import model_to_dict

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

# instead of manually converting each field of model into key-value pair in dic, we can simply use model_to_dict to do that work for me
# JsonResponse accepts a python dictionary as an argument
# HttpResponse accepts a string as an argument
# For doing the above thing, if type is Decimal, then json.dumps(data) will also not help us in converting Decimal to str 

def api_home(request: HttpRequest, *args, **kwargs):
    params = dict(request.GET)
    print(params['title'])
    products = Product.objects.all().order_by("?")
    print(products)
    data = {}
    for product in products:
        if product.title == params['title'][0]:
            data = model_to_dict(product, fields=['id', 'title', 'content', 'price'])
            # data['id'] = product.id
            # data['title'] = product.title
            # data['content'] = product.content
            # data['price'] = str(product.price)
    # print(data.keys())
    # json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={'content-type':'application/json'})
    return JsonResponse(data)