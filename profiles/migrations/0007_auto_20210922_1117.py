# Generated by Django 3.2.7 on 2021-09-22 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='notification',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
