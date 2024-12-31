import requests
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
import json

BASE_SERVER_URL = 'https://backend-tasks-9r0i.onrender.com/'

@csrf_exempt
def proxy_view(request, path=""):
    url = BASE_SERVER_URL + path
    headers = {key: value for key, value in request.headers.items() if key.lower() != 'host'}

    try:
        if request.method == 'GET':
            response = requests.get(url, headers=headers, params=request.GET)
        elif request.method == 'HEAD':
            response = requests.head(url, headers=headers)
        elif request.method == 'POST':
            if request.content_type == 'application/json':
                response = requests.post(url, headers=headers, json=json.loads(request.body.decode('utf-8')))
            else:
                data = QueryDict(request.body)
                response = requests.post(url, headers=headers, data=data)
        elif request.method == 'PUT':
            response = requests.put(url, headers=headers, json=json.loads(request.body.decode('utf-8')))
        elif request.method == 'DELETE':
            response = requests.delete(url, headers=headers)
        else:
            return JsonResponse({'error': 'Unsupported HTTP method'}, status=405)

        return HttpResponse(
            response.content,
            status=response.status_code,
            content_type=response.headers.get('Content-Type', 'text/plain')
        )
    except requests.RequestException as e:
        return JsonResponse({'error': 'Failed to connect to the main server', 'details': str(e)}, status=500)