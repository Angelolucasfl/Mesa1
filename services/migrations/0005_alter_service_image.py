# Generated by Django 4.2.2 on 2023-06-27 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_remove_contractor_address_service_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(default='media/service_images/default.jpg', upload_to='media/service_images/'),
        ),
    ]
