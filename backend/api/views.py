import json
from django.http import JsonResponse


# request -> It is an instance of HttpRequest -> Django # Nothing to do with python requests
# request.body gives byte string JSON data

def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data.keys())
    return JsonResponse(data)
