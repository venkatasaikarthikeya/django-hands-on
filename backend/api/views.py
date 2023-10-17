import json
from django.http import JsonResponse, HttpResponse
from django.http import HttpRequest
from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer

from todos.models import Todo
from todos.serializers import TodoSerializer

from rest_framework.views import APIView


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

""" def api_home(request: HttpRequest, *args, **kwargs):
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
    return JsonResponse(data) """



# @api_view's http_method_names is highly useful, in the sense that it doesn't allow requests of method types which are not in this list
# Response is from rest_framework, it also takes a python dict as an argument and returns json

# @api_view(http_method_names=["GET"])
# def api_home(request: HttpRequest, *args, **kwargs):
#     # If we didn't have http_method_names on decorator, we might have to manually handle correct method checks as below
#     # if request.method == "POST":
#     #     return Response({"detail": "Method \"POST\" not allowed."}, status=405)
#     """ product = Product.objects.all().order_by("?").first()
#     data = {}
#     if product:
#         # The property sale_price is not being returned. This is one of the places where Serializers can help. So, fields will only work for variables.
#         data = model_to_dict(product, fields=['id', 'title', 'content', 'price', 'sale_price']) """
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data
#     return Response(data)


# Serializers can also take data in, clean it up and ensure that data is correct and right.
# DRF doesn't require CSRF token to be set on a post request

@api_view(http_method_names=["POST"])
def api_home(request: HttpRequest, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        data = ProductSerializer(instance).data
        return Response(data)
    return Response({"Invalid Request": "Not good data"}, status=400)


# Backend for todo application


@api_view(http_method_names=['GET', 'POST', 'PUT', 'DELETE'])
def api_todo(request: HttpRequest, *args, **kwargs):
    if request.method == 'GET':
        request_params = dict(request.GET)
        if not request_params:
            return Response({'Invalid Request': 'Params not found'}, status=400)
        if 'id' in request_params.keys():
            target_id = request_params['id'][0]
            instance = Todo.objects.get(id=target_id)
            if instance:
                data = TodoSerializer(instance).data
                return Response(data, status=200)
        return Response({'Resource Error': 'The content you have requested for no longer exists'}, status=400)
    # elif request.method == 'POST':

    # elif request.method == 'PUT':

    # elif request.method == 'DELETE':
    # data = {}
    # instance = Todo.objects.all().first()
    # if instance:
    #     # data = model_to_dict(instance, fields=['id', 'title', 'description', 'status', 'get_summary'])
    #     data = TodoSerializer(instance).data
    #     return Response(data, status=200)
    # return Response({"Invalid Request": "Server Error"}, status=400)


class TodoView(APIView):


    def get(self, request: HttpRequest) -> Response:
        request_params = dict(request.GET)
        if not request_params:
            return Response({'Invalid Request': 'Params not found'}, status=400)
        if 'id' in request_params.keys():
            target_id = request_params['id'][0]
            instance = Todo.objects.get(id=target_id)
            if instance:
                data = TodoSerializer(instance).data
                return Response(data, status=200)
        return Response({'Resource Error': 'The content you have requested for no longer exists'}, status=400)
    

    def post(self, request: HttpRequest) -> Response:
        request_body = request.data
        serializer = TodoSerializer(data=request_body)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            data = TodoSerializer(instance).data
            return Response(data, status=200)
        return Response({"Server Error": "Invalid Request"}, status=400)
    

    def put(self, request: HttpRequest) -> Response:
        request_body = request.data
        updatable_todo = dict(request_body)
        stored_instance = None
        try:
            stored_instance = Todo.objects.get(id=updatable_todo['id'])
        except:
            return Response({'Resource Error': 'The content you have requested for no longer exists'}, status=400)
        serializer = TodoSerializer(stored_instance, data=request_body)
        if serializer.is_valid(raise_exception=True):
            updated_instance = serializer.save()
            data = TodoSerializer(updated_instance).data
            return Response(data, status=200)
        return Response({'Server Error': 'Invalid Request'}, status=400)
    

    def delete(self, request: HttpRequest) -> Response:
        request_params = dict(request.GET)
        if not request_params:
            return Response({'Invalid Request': 'Params not found'}, status=400)
        if 'id' in request_params.keys():
            target_id = request_params['id'][0]
            instance = None
            try:
                instance = Todo.objects.get(id=target_id)
                instance.delete()
                return Response({'Success': 'Deleted!!'})
            except:
                return Response({'Resource Error': 'The content you have requested for no longer exists'}, status=400)


