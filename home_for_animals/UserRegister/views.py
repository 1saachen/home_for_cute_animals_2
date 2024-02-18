from django.shortcuts import redirect  # 导入 redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, throttling
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from .models import User
from .forms import UserRegisterForm, UserLoginForm  # 修改表单的导入
from rest_framework.authtoken.views import ObtainAuthToken

class UserRegistrationAPIView(APIView):
    def post(self, request):
        # 创建一个UserRegisterForm实例并将请求数据传递给它
        form = UserRegisterForm(request.data)  # 使用正确的表单类

        # 检查表单是否有效
        if form.is_valid():
            # 从表单中提取验证过的数据
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # 检查用户名是否已经存在
            if User.objects.filter(username=username).exists():
                return Response({'error': '用户名已存在。'}, status=status.HTTP_400_BAD_REQUEST)

            # 检查邮箱是否已经存在
            if User.objects.filter(email=email).exists():
                return Response({'error': '邮箱已存在。'}, status=status.HTTP_400_BAD_REQUEST)

            # 创建用户
            hashed_password = make_password(password)
            user = User.objects.create(username=username, email=email, password=hashed_password)

            return Response({'message': '用户注册成功。'}, status=status.HTTP_201_CREATED)
        else:
            # 如果表单无效，则返回表单错误
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    def post(self, request):
        form = UserLoginForm(request.data)  # 使用正确的表单类
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                return Response({'error': '用户名或密码无效。'}, status=status.HTTP_400_BAD_REQUEST)
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect("list")  # 使用 redirect 函数重定向

class CustomThrottle(throttling.SimpleRateThrottle):
    scope = 'login_attempts'

    def allow_request(self, request, view):
        if request.user.is_authenticated:
            return True
        ip = self.get_ident(request)
        last_login_attempt = self.history.get(ip, [])
        attempts = len(last_login_attempt)
        max_attempts = 3
        if attempts >= max_attempts:
            return False
        else:
            now = timezone.now()
            self.history[ip] = last_login_attempt + [now]
            return True

class CustomObtainAuthToken(ObtainAuthToken):
    throttle_classes = [CustomThrottle]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            try:
                token = Token.objects.get(key=response.data['token'])
                token.created = timezone.now()
                token.save()
            except KeyError:
                pass  # 处理键错误异常
        return response


