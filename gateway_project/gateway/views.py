
import requests
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

FIRST_SERVER_URL = 'https://backend-tasks-9r0i.onrender.com/'

@csrf_exempt
def gateway_view(request, path=''):
    url = f"{FIRST_SERVER_URL}/{path}" 
    
    try:
        if request.method == "GET":
            response = requests.get(url, params=request.GET)
        elif request.method == "HEAD":
            response = requests.head(url, headers=request.headers)
        elif request.method == "POST":
            response = requests.post(url, json=request.body, headers=request.headers)
        elif request.method == "DELETE":
            response = requests.delete(url, headers=request.headers)
        else:
            return JsonResponse({"error": "Метод не поддерживается"}, status=405)

        return HttpResponse(
            response.content,
            status=response.status_code,
            content_type=response.headers.get('Content-Type', 'application/json')
        )
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)