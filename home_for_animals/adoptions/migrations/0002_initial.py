# Generated by Django 5.0.2 on 2024-02-19 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("adoptions", "0001_initial"),
        ("pets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="adoptionrequest",
            name="pet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="pets.pet",
                verbose_name="宠物",
            ),
        ),
    ]