import requests
from django.http import HttpResponse

FIRST_SERVER_URL = "https://backend-tasks-9r0i.onrender.com"

def proxy_to_first_server(request, endpoint):
    url = f"{FIRST_SERVER_URL}/{endpoint}"
    method = request.method
    headers = request.headers
    data = request.body

    response = requests.request(method, url, headers=headers, data=data)

    return HttpResponse(
        response.content,
        status=response.status_code,
        content_type=response.headers.get('Content-Type', 'application/json')
    )