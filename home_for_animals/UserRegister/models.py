from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Permission
from django.db import models



class CustomUser(AbstractUser):
    login_attempts = models.PositiveIntegerField(default=0)  # 记录登录尝试次数
    locked = models.BooleanField(default=False)  # 记录用户是否被锁定

    def increment_login_attempts(self):
        self.login_attempts += 1
        self.save()

    def reset_login_attempts(self):
        self.login_attempts = 0
        self.save()

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='customuser_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_user_permissions'
    )


class User(models.Model):
    username=models.CharField(max_length=100, unique=True)
    password=models.CharField(max_length=100)
