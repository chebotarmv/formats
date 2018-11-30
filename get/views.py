from django.http import HttpResponse
import json

def get(request):
    if request.method == 'GET':
        message = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}
        return HttpResponse(json.dumps(message))