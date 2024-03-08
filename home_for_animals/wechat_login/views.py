from django.http import JsonResponse
from .models import User
import requests
import json

def wechat_login(request):
    code = request.GET.get('code')
    if not code:
        return JsonResponse({'error': '缺少 code 参数'}, status=400)

    appid = 'wx16afb46c6068a4dd'
    secret = '65bc34bcd1df8bfdd73de1bd1fae31ab'
    url = f'https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type=authorization_code'

    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查是否有错误响应
        data = response.json()

        openid = data.get('openid')
        session_key = data.get('session_key')

        # 保存用户信息到数据库
        if openid and session_key:
            save_user_info(openid, session_key)

        return JsonResponse({'openid': openid, 'session_key': session_key})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': '向微信服务器发送请求失败'}, status=500)
    except json.JSONDecodeError as e:
        return JsonResponse({'error': '解析微信服务器响应失败'}, status=500)

def save_user_info(openid, session_key):
    user, created = User.objects.get_or_create(openid=openid)
    if created:
        user.session_key = session_key
        user.save()



