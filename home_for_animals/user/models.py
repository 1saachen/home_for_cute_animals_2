from django.db import models
from zq_django_util.utils.user.models import AbstractUser

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

    nick_name = models.CharField(max_length=20, blank=True,
                                 verbose_name="昵称")

    avatar = models.ImageField(upload_to=r"user\avatar",
                               default=r"user\avatar\default.jpg",
                               verbose_name="头像",
    )

    """
    额外信息
    """
    real_name = models.CharField(max_length=10, blank=True,
                                 null=True,
                                 verbose_name="真实姓名")

    gender = models.CharField(max_length=10, blank=True,
                              null=True,
                              choices=(('male', "男"), ('female', "女")),
                              verbose_name="性别")

    id_card = models.CharField(max_length=18, blank=True,
                               null=True, unique=True,
                               verbose_name="身份证号")
    phone = models.CharField(max_length=20, blank=True,
                             null=True, unique=True,
                             verbose_name="手机号")
    email = models.EmailField(blank=True, null=True,
                              unique=True,
                              verbose_name="邮箱")
    signature = models.TextField(max_length=100, blank=True,
                                 null=True,
                                 verbose_name="个性签名")
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

