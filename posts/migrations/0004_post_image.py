# Generated by Django 3.2.7 on 2021-09-21 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210918_0608'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='images/profile-small-1.jpg', null=True, upload_to='images'),
        ),
    ]
