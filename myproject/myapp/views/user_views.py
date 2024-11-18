from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.http import QueryDict
from django.http.multipartparser import MultiPartParser
import json
import re

def index(request):
    return JsonResponse({'message': 'Welcome to the Cat API!'})

@csrf_exempt
@require_http_methods(["GET"])
def get_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
        return JsonResponse(user_data)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
def create_user(username, password, email, first_name, last_name):
    # Вызов функций для проверки каждого поля
    validate_username(username)
    validate_password(password)
    validate_email(email)
    validate_first_name(first_name)
    validate_last_name(last_name)

    # Создание пользователя
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name
    )
    return user
    
@csrf_exempt
@require_http_methods(["PUT"])
def update_user(request, user_id):
    try:

        print("request.POST:", request.POST)
        print("request.body:", request.body)
        print("content_type:", request.content_type)
        user = User.objects.get(id=user_id)

        if request.content_type.startswith('multipart/form-data'):
            parser = MultiPartParser(request.META, request, request.upload_handlers)
            data, _ = parser.parse()
        elif request.content_type == 'application/x-www-form-urlencoded':
            data = QueryDict(request.body, encoding=request.encoding)
        elif request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            return JsonResponse({'error': 'Unsupported content type'}, status=400)

        print("Received data for update:", data)

        updated_fields = {}

        if 'username' in data:
            if validate_username:
                user.username = data['username']
                updated_fields['username'] = user.username

        if 'email' in data:
            if validate_email:
                user.email = data['email']
                updated_fields['email'] = user.email

        if 'first_name' in data:
            if validate_first_name:
                user.first_name = data['first_name']
                updated_fields['first_name'] = user.first_name

        if 'last_name' in data:
            if validate_last_name:
                user.last_name = data['last_name']
                updated_fields['last_name'] = user.last_name

        if 'password' in data:
            password = data['password']
            if validate_password:
                user.set_password(password)
                updated_fields['password'] = '***'

        if updated_fields:
            user.save()
            print("Updated user data:", updated_fields)
            return JsonResponse({'message': 'User updated successfully', 'updated_fields': updated_fields})
        else:
            return JsonResponse({'message': 'No changes made to the user'}, status=200)

    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    except ValidationError as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

def validate_username(username, check_existence=True):
    if not username:
        raise ValidationError('Username is required')
    if not re.match(r'^[A-Za-z]{4,10}$', username):
        raise ValidationError('Username must be between 4 and 10 characters long and contain only Latin letters')
    if check_existence and User.objects.filter(username=username).exists():
        raise ValidationError('Username already exists')
    return True

def validate_password(password):
    if not password:
        raise ValidationError('Password is required')
    if len(password) < 8:
        raise ValidationError('Password must be at least 8 characters long')
    if not re.search(r'[A-Z]', password):
        raise ValidationError('Password must contain at least one uppercase letter')
    if not re.search(r'[a-z]', password):
        raise ValidationError('Password must contain at least one lowercase letter')
    if not re.search(r'\d', password):
        raise ValidationError('Password must contain at least one digit')
    if not re.match(r'^[A-Za-z0-9]+$', password):
        raise ValidationError('Password must contain only Latin letters and digits')
    return True

def validate_email(email):
    if not email:
        raise ValidationError('Email is required')
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_pattern, email):
        raise ValidationError('Invalid email format')
    return True

def validate_first_name(first_name):
    if not first_name:
        raise ValidationError('First name is required')
    return True

def validate_last_name(last_name):
    if not last_name:
        raise ValidationError('Last name is required')
    return True