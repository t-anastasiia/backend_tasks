from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

BASE_SERVER_URL = 'https://backend-tasks-9r0i.onrender.com/'

@csrf_exempt
def root_view(request):
    if request.method == 'HEAD' or request.method == 'GET':
        url = BASE_SERVER_URL  
        headers = {key: value for key, value in request.headers.items() if key.lower() != 'host'}

@csrf_exempt
def proxy_view(request, path=""):
    url = BASE_SERVER_URL + path
    headers = {key: value for key, value in request.headers.items() if key.lower() != 'host'}

    try:
        if request.method == 'GET':
            response = requests.get(url, headers=headers, params=request.GET, stream=True)
        elif request.method == 'POST':
            response = requests.post(url, headers=headers, data=request.body, stream=True)
        elif request.method == 'PUT':
            response = requests.put(url, headers=headers, data=request.body, stream=True)
        elif request.method == 'DELETE':
            response = requests.delete(url, headers=headers, stream=True)
        else:
            return JsonResponse({'error': 'Unsupported HTTP method'}, status=405)

        django_response = HttpResponse(
            response.raw,  
            status=response.status_code,
            content_type=response.headers.get('Content-Type')
        )
        
        for header, value in response.headers.items():
            if header.lower() not in ['content-encoding', 'transfer-encoding', 'content-length']:
                django_response[header] = value

        return django_response

    except requests.RequestException as e:
        return JsonResponse({'error': 'Failed to connect to the main server', 'details': str(e)}, status=500)