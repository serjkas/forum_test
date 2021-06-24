from django.urls import path
from .views import get_users_forum

urlpatterns = [
    path('', get_users_forum),
]
