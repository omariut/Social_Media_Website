# Generated by Django 3.2.7 on 2021-09-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='images/profile-small-1.jpg', null=True, upload_to='images'),
        ),
    ]
