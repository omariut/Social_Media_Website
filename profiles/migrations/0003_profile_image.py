# Generated by Django 3.2.7 on 2021-09-18 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210917_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
