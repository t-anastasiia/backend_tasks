import requests
from django.http import JsonResponse, HttpResponse

FIRST_SERVER_URL = "https://backend-tasks-9r0i.onrender.com"

def proxy_to_backend(request, endpoint):
    url = f"{FIRST_SERVER_URL}/{endpoint}"
    method = request.method
    headers = {
        key: value for key, value in request.headers.items()
        if key != 'Host'  # Исключаем заголовок Host
    }
    data = request.body if method in ['POST', 'PUT', 'PATCH'] else None

    try:
        response = requests.request(method, url, headers=headers, data=data)
        return HttpResponse(
            response.content,
            status=response.status_code,
            content_type=response.headers.get('Content-Type', 'application/json')
        )
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=502)