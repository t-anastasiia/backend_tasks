from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.proxy_home, name='home'), 
    re_path(r'^(?P<endpoint>.+)/$', views.proxy_to_backend, name='proxy_to_backend'), 
]