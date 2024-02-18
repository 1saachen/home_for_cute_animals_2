# UserRegister/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationAPIView.as_view(), name='user_register'),
    path('login/', views.UserLoginAPIView.as_view(), name='user_login'),
]

