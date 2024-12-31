from django.urls import path
from . import views

urlpatterns = [
    path('', views.proxy_home, name='home'),
    path('proxy/<path:endpoint>/', views.proxy_to_first_server, name='proxy'),
]