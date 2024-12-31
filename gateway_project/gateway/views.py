import requests
from django.http import HttpResponse

FIRST_SERVER_URL = "https://backend-tasks-9r0i.onrender.com"

def proxy_home(request):
    response = requests.get(FIRST_SERVER_URL)
    return HttpResponse(
        response.content,
        status=response.status_code,
        content_type=response.headers.get('Content-Type', 'application/json')
    )