# Generated by Django 5.0.2 on 2024-02-17 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('donor_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('target_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='adoption',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='Accounting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_date', models.DateTimeField(auto_now_add=True)),
                ('donation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.donation')),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.project'),
        ),
    ]
