from django.db import models
from django.utils import timezone
# from zq_django_util.utils.user.models import AbstractUser
from django.contrib.auth.models import AbstractUser
# from utils.choices.types import GenderType
class User(AbstractUser):
    """
    基本用户表
    """
    # 自定义字段
    # extra-checks-disable-next-line field-text-null
    openid = models.CharField(
        max_length=64, unique=True, null=True, verbose_name="微信openid"
    )

    union_id = models.UUIDField(
        unique=True, null=True, blank=True, verbose_name="自强union_id"
    )

    # create_time = models.DateTimeField(default=timezone.now,
    #                                    verbose_name="创建时间",
    #                                    editable=False)
    # update_time = models.DateTimeField(auto_now=True,
    #                                    verbose_name="更新时间")
    # def save(self, *args, **kwargs):
    #     if not self.create_time:
    #         self.create_time = timezone.now()
    #     self.update_time = timezone.now()
    #     return super(User, self).save(*args, **kwargs)

    nick_name = models.CharField(max_length=20, blank=True, verbose_name="昵称")

    avatar = models.ImageField(
        upload_to="user/avatar",
        default="user/avatar/default.jpg",
        verbose_name="头像",
    )

    """
    额外信息
    """
    real_name = models.CharField(
        max_length=10, blank=True, null=True, verbose_name="真实姓名"
    )

    gender = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=(("male", "男"), ("female", "女")),
        verbose_name="性别",
    )

    id_card = models.CharField(
        max_length=18, blank=True, null=True, unique=True, verbose_name="身份证号"
    )
    phone = models.CharField(
        max_length=20, blank=True, null=True, unique=True, verbose_name="手机号"
    )
    email = models.EmailField(
        blank=True, null=True, unique=True, verbose_name="邮箱"
    )
    signature = models.TextField(
        max_length=100, blank=True, null=True, verbose_name="个性签名"
    )
    # class Meta:
    #     app_label = "users"
    #     db_table = "zq_user"
    #     verbose_name = "用户"
    #     verbose_name_plural = verbose_name

    class Meta:
        app_label = "users"
        verbose_name = " 个人信息 "
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class VolunteerRecord(models.Model):
    """
    志愿记录
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=255)
    volunteer_date = models.DateField()
    hours = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.activity}"


class DonationRecord(models.Model):
    """
    捐赠记录
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - ${self.amount}"

# class ChatMessage(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_messages')
#     message = models.TextField(max_length=1000)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f'{self.user} - {self.timestamp}'
# class Feedback(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='feedbacks')
#     feedback_text = models.TextField(max_length=1000)
#     submitted_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f'Feedback from {self.user} at {self.submitted_at}'
