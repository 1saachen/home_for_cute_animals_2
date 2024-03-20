# Generated by Django 5.0.2 on 2024-03-20 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0006_pet_condition_pet_social_pet_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="SelectedAnimals",
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
                ("date", models.DateField()),
                ("status", models.CharField(blank=True, max_length=20, null=True)),
                ("applications", models.IntegerField(default=0)),
                ("requirements", models.TextField()),
                (
                    "pet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="selected_animals",
                        to="pets.pet",
                    ),
                ),
            ],
        ),
    ]