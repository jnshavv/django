# Generated by Django 4.1.3 on 2023-02-23 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0011_booking_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total',
            field=models.IntegerField(default=1),
        ),
    ]
