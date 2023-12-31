# Generated by Django 4.2.2 on 2023-06-26 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_service_enlisted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='enlisted',
            field=models.ManyToManyField(to='services.employee'),
        ),
        migrations.AlterField(
            model_name='service',
            name='hours',
            field=models.TimeField(),
        ),
    ]
