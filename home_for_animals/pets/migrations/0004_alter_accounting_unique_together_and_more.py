# Generated by Django 5.0.2 on 2024-02-18 10:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_donation_project_alter_adoption_unique_together_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='accounting',
            unique_together={('donation', 'donation_date')},
        ),
        migrations.AlterUniqueTogether(
            name='adoption',
            unique_together={('pet', 'user')},
        ),
    ]