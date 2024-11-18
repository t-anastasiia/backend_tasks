from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return JsonResponse({'message': 'Welcome to the Cat API!'})

@csrf_exempt
def cat_info(request):
    if request.method == 'GET':
        # Обработка GET запроса
        return JsonResponse({'message': 'This is the cat info page. Send data about cats!'})

    elif request.method == 'POST':
        # Обработка POST запроса и редирект
        try:
            data = json.loads(request.body) if request.content_type == 'application/json' else request.POST
            breed = data.get('breed')
            rating = data.get('rating')
            image_url = data.get('image_url')

            if not breed or not rating or not image_url:
                return JsonResponse({'error': 'Missing required fields: breed, rating, image_url'}, status=400)
            # Вывод полученной информации
            received_info = {
                'breed': breed,
                'rating': rating,
                'image_url': image_url
            }

            # Редирект с отображением полученной информации
            return JsonResponse({'message': 'Cat data received successfully', 'data': received_info})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
def get_endpoint1(request):
    return JsonResponse({'message': 'This is GET endpoint 1'})

def get_endpoint2(request):
    return JsonResponse({'message': 'This is GET endpoint 2'})