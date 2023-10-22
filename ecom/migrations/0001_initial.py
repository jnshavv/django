# Generated by Django 4.1.3 on 2023-02-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='my images')),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField()),
            ],
            options={
                'db_table': 'dest',
            },
        ),
    ]