from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings  # 引入 settings

# 自定义用户模型
class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars/', null=True, blank=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
