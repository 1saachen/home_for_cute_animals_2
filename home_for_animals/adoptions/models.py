from django.db import models

from apps.users.models import User
from apps.pets.models import Pet

class AdoptionRequest(models.Model):
    """
    领养申请
    """
    # ?
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, verbose_name='宠物')
    request_date = models.DateTimeField(auto_now_add=True, verbose_name='申请日期')
    status = models.CharField(max_length=10,
                              choices=(('pending', '正在审核'),
                                       ('approved', '审核通过'),
                                       ('rejected', '审核不通过')),
                              default='pending',
                              verbose_name='审核状态')

    class Meta:
        verbose_name = '领养申请'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.user} 的领养申请 - {self.pet}"

