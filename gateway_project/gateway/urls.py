from django.urls import re_path
from .views import GatewayView

urlpatterns = [
    re_path(r'.*', GatewayView.as_view(), name='gateway'),
]