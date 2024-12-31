from django.http import HttpResponse

def home(request):
    if request.method == 'HEAD':
        response = HttpResponse("Welcome to the homepage!")
        response['Content-Length'] = len(response.content)  
        return response
    elif request.method == 'GET':
        return HttpResponse("Welcome to the homepage!")
    else:
        return HttpResponse("Method Not Allowed", status=405)