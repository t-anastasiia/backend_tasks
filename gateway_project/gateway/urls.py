from django.urls import path
from .views import root_view, proxy_view

urlpatterns = [
    path('', root_view, name='home'), 
    path('<path:path>', proxy_view, name='proxy'), 
]