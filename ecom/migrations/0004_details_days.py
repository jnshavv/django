# Generated by Django 4.1.3 on 2023-02-16 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_details_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='days',
            field=models.CharField(default='', max_length=20),
        ),
    ]
