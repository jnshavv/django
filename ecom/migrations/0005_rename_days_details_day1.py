# Generated by Django 4.1.3 on 2023-02-17 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_details_days'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='days',
            new_name='day1',
        ),
    ]