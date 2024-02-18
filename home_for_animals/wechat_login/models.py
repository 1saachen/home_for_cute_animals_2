from django.db import models

class User(models.Model):
    openid = models.CharField(max_length=100, unique=True)  # 用户唯一标识 OpenID
    session_key = models.CharField(max_length=100)  # 会话密钥 SessionKey
    nickname = models.CharField(max_length=100, blank=True)  # 用户昵称，允许为空
    avatar_url = models.URLField(blank=True)  # 用户头像链接，允许为空
    gender = models.CharField(max_length=10, choices=[('male', '男'), ('female', '女'), ('unknown', '未知')], default='unknown')  # 用户性别，默认为未知
    created_at = models.DateTimeField(auto_now_add=True)  # 用户创建时间

    def __str__(self):
        return self.openid


# Create your models here.
