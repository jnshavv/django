# Generated by Django 4.1.3 on 2023-02-16 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='title',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]