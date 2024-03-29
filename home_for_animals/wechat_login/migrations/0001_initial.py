# Generated by Django 5.0.2 on 2024-02-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=100, unique=True)),
                ('session_key', models.CharField(max_length=100)),
                ('nickname', models.CharField(blank=True, max_length=100)),
                ('avatar_url', models.URLField(blank=True)),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女'), ('unknown', '未知')], default='unknown', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
