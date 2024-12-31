from django.urls import path
from .views import proxy_view

urlpatterns = [
    path('', proxy_view, {'path': ''}),  # Корневой путь
    path('<path:path>', proxy_view),     # Все остальные пути
]