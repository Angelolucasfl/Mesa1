# Generated by Django 4.2.2 on 2023-07-12 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_service_chosen_employee_alter_service_enlisted'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
