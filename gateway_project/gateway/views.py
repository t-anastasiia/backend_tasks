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

        logger.info(f"Content-Type from server: {response.headers.get('Content-Type')}")
        logger.info(f"Raw content: {response.content}")

        content_type = response.headers.get('Content-Type', 'text/plain')

        if content_type.startswith('text/'):
            decoded_content = response.content.decode('utf-8', errors='replace')
            return HttpResponse(
                decoded_content,
                status=response.status_code,
                content_type=content_type
            )

        return HttpResponse(
            response.content,
            status=response.status_code,
            content_type=content_type
        )

    except requests.exceptions.RequestException as e:
        logger.error(f"Error while forwarding request: {e}")
        return JsonResponse({"error": str(e)}, status=500)