from django.urls import path
from .views import (
    home, register, login_user, logout_user,
    create_user, get_user, update_user, delete_user,
    cat_info, get_endpoint1, get_endpoint2
)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get_user/<int:user_id>/', get_user, name='get_user'),
    path('update_user/<int:user_id>/', update_user, name='update_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('cat_info/', cat_info, name='cat_info'),
    path('get1/', get_endpoint1, name='get1'),
    path('get2/', get_endpoint2, name='get2'),
]