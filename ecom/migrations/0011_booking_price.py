# Generated by Django 4.1.3 on 2023-02-20 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0010_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.IntegerField(default=1),
        ),
    ]
