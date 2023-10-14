from django.http import JsonResponse


def api_home(requests, *args, **kwargs):
    response = {'query': 'Hello World'}
    return JsonResponse(response)
