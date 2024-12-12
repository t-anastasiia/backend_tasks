from django.http import HttpResponse, JsonResponse
import requests
import logging

FIRST_SERVER_URL = "https://backend-tasks-9r0i.onrender.com"
logger = logging.getLogger(__name__)

def proxy(request, path=""):
    method = request.method
    data = request.body
    headers = {key: value for key, value in request.headers.items() if key.lower() != 'host'}

    try:
        response = requests.request(
            method,
            f"{FIRST_SERVER_URL}/{path}",
            data=data,
            headers=headers
        )
        return HttpResponse(
            response.content.decode('utf-8'),  
            status=response.status_code,
            content_type="text/plain"
        )
    except requests.exceptions.RequestException as e:
        logger.error(f"Error while forwarding request: {e}")
        return JsonResponse({"error": str(e)}, status=500)