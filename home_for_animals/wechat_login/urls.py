from django.urls import path
from . import views

urlpatterns = [
    path('wechat_login/', views.wechat_login, name='wechat_login'),
]
