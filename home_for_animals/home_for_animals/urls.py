"""home_for_animals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('user/',include('users.urls')),
    path('pets/', include('pets.urls')),  # 包含 pets 应用的 urls.py 文件
    path('UserRegister/', include('UserRegister.urls')),  # 使用UserRegister应用中的UserRegister视图函数
    path('wechat_login/',include('wechat_login.urls') ),  # 使用UserRegister应用中的wechat_login视图函数
]
