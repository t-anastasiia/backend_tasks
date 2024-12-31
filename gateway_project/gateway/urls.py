from django.urls import re_path
from .views import proxy_request

urlpatterns = [
    # Прокси для всех запросов
    re_path(r'^(?P<path>.*)$', proxy_request, name="proxy_request"),
]