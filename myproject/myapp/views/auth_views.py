from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.http import JsonResponse
import json

# Импорт create_user из user_views
from .user_views import create_user

@csrf_exempt
@require_http_methods(["POST"])
def register(request):
    try:
        # Сбор данных из запроса
        if request.content_type.startswith('multipart/form-data') or request.content_type == 'application/x-www-form-urlencoded':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
        else:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')
            first_name = data.get('first_name')
            last_name = data.get('last_name')

        # Проверка наличия всех необходимых полей
        if not all([username, password, email, first_name, last_name]):
            return JsonResponse({'error': 'All fields (username, password, email, first_name, last_name) are required'}, status=400)

        # Вызов функции создания пользователя с валидацией
        user = create_user(username, password, email, first_name, last_name)
        return JsonResponse({'message': 'User registered successfully', 'user_id': user.id}, status=201)

    except ValidationError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Failed to create user: {str(e)}'}, status=500)
    
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        if request.content_type.startswith('multipart/form-data') or request.content_type == 'application/x-www-form-urlencoded':
            username = request.POST.get('username')
            password = request.POST.get('password')
        else:
            try:
                data = json.loads(request.body)
                username = data.get('username')
                password = data.get('password')
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        if not username or not password:
            return JsonResponse({'error': 'Username and password are required'}, status=400)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)

@csrf_exempt
def logout_user(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request)
            return JsonResponse({'message': 'Logout successful'})
        else:
            return JsonResponse({'error': 'No active session found. Please log in first.'}, status=400)