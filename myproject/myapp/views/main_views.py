from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    if request.method == 'HEAD':
        response = HttpResponse("Приветики это head для корневого пути")
        response['Content-Length'] = len(response.content)  
        response.content = b'' 
        return response
    elif request.method == 'GET':
        return HttpResponse("Приветики это get для корневого пути")
    else:
        return HttpResponse("Извините, а такое тут нельзя", status=405)