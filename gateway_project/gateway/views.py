import requests
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# URL основного сервера
BASE_SERVER_URL = "https://backend-tasks-9r0i.onrender.com"

@csrf_exempt
def proxy_request(request, path=""):
    """Перенаправление запросов на основной сервер."""
    # Формируем конечный URL
    target_url = f"{BASE_SERVER_URL}{path}"
    
    try:
        # Проверяем метод запроса и перенаправляем
        if request.method == "GET":
            response = requests.get(target_url, params=request.GET)
        elif request.method == "POST":
            response = requests.post(target_url, data=request.body, headers={"Content-Type": request.headers.get("Content-Type")})
        elif request.method == "HEAD":
            response = requests.head(target_url, headers=request.headers)
        elif request.method == "DELETE":
            response = requests.delete(target_url, headers=request.headers)
        else:
            return JsonResponse({"error": "Метод не поддерживается"}, status=405)

        # Возвращаем ответ клиенту
        return HttpResponse(
            response.content,
            status=response.status_code,
            content_type=response.headers.get("Content-Type", "application/json")
        )
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"Ошибка проксирования: {str(e)}"}, status=500)