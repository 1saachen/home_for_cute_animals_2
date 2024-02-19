# Generated by Django 4.1.4 on 2022-12-23 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RequestLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="用户ID"
                    ),
                ),
                ("ip", models.CharField(max_length=32, verbose_name="用户IP")),
                (
                    "method",
                    models.CharField(max_length=32, verbose_name="请求方法"),
                ),
                ("url", models.TextField(verbose_name="请求URL")),
                ("headers", models.JSONField(verbose_name="请求头")),
                (
                    "content_type",
                    models.CharField(max_length=32, verbose_name="请求类型"),
                ),
                ("query_param", models.JSONField(verbose_name="请求参数")),
                ("request_body", models.JSONField(verbose_name="请求数据")),
                ("file_data", models.JSONField(verbose_name="文件数据")),
                ("response", models.JSONField(verbose_name="响应数据")),
                (
                    "status_code",
                    models.PositiveSmallIntegerField(
                        db_index=True, verbose_name="响应状态码"
                    ),
                ),
                (
                    "execution_time",
                    models.DecimalField(
                        decimal_places=5,
                        max_digits=8,
                        null=True,
                        verbose_name="执行时间",
                    ),
                ),
                (
                    "create_time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="请求时间"
                    ),
                ),
            ],
            options={
                "verbose_name": "请求日志",
                "verbose_name_plural": "请求日志",
                "db_table": "log_request",
                "ordering": ["-create_time"],
            },
        ),
        migrations.CreateModel(
            name="ExceptionLog",
            fields=[
                (
                    "requestlog_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="logs.requestlog",
                    ),
                ),
                (
                    "exp_id",
                    models.CharField(max_length=32, verbose_name="异常ID"),
                ),
                (
                    "exception_type",
                    models.CharField(max_length=128, verbose_name="异常类型"),
                ),
                (
                    "event_id",
                    models.CharField(max_length=32, verbose_name="Sentry事件ID"),
                ),
                ("exception_msg", models.TextField(verbose_name="异常信息")),
                ("exception_info", models.TextField(verbose_name="异常详情")),
                ("stack_info", models.JSONField(verbose_name="异常栈")),
            ],
            options={
                "verbose_name": "异常日志",
                "verbose_name_plural": "异常日志",
                "db_table": "log_exception",
                "ordering": ["-create_time"],
            },
            bases=("logs.requestlog",),
        ),
    ]
