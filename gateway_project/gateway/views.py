import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

FIRST_SERVER_URL = "https://backend-tasks-9r0i.onrender.com"

class GatewayView(APIView):
    def forward_request(self, request, endpoint):
        url = f"{FIRST_SERVER_URL}/{endpoint}"
        method = request.method
        headers = {
            key: value for key, value in request.headers.items() if key != 'Host'
        }
        data = request.data if method in ['POST', 'PUT', 'PATCH'] else None

        try:
            response = requests.request(method, url, headers=headers, data=data)
            return Response(
                data=response.json() if response.content else None,
                status=response.status_code,
                content_type=response.headers.get('Content-Type')
            )
        except requests.exceptions.RequestException as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_502_BAD_GATEWAY
            )

    def get(self, request, *args, **kwargs):
        endpoint = request.path_info.lstrip('/')  # Убираем ведущий слэш
        return self.forward_request(request, endpoint)

    def post(self, request, *args, **kwargs):
        endpoint = request.path_info.lstrip('/')  # Убираем ведущий слэш
        return self.forward_request(request, endpoint)