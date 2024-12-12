from django.http import JsonResponse, HttpResponse
import requests

FIRST_SERVER_URL = "https://backend-tasks-9r0i.onrender.com"

def proxy(request, path=""):
    method = request.method  
    data = request.body 
    headers = {key: value for key, value in request.headers.items() if key != 'Host'}

    try:
        response = requests.request(
            method,
            f"{FIRST_SERVER_URL}/{path}",
            data=data,
            headers=headers
        )
        return HttpResponse(
            response.content,
            status=response.status_code,
            content_type=response.headers.get('Content-Type', 'application/json')
        )
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)