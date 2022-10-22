# Generated by Django 3.2.14 on 2022-08-14 06:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="message",
            name="pending_read",
            field=models.ManyToManyField(
                related_name="unread_messages", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="pending_reception",
            field=models.ManyToManyField(
                related_name="pending_messages", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="body",
            field=models.TextField(blank=True, default="", max_length=500, null=True),
        ),
    ]