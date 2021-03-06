# Generated by Django 3.2.7 on 2021-09-19 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0003_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='receiver',
        ),
        migrations.AddField(
            model_name='relationship',
            name='receiver',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='sender',
        ),
        migrations.AddField(
            model_name='relationship',
            name='sender',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
