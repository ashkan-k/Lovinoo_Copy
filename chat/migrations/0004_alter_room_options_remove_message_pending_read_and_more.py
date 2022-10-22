# Generated by Django 4.1 on 2022-08-17 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0003_auto_20220814_1100"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="room",
            options={},
        ),
        migrations.RemoveField(
            model_name="message",
            name="pending_read",
        ),
        migrations.RemoveField(
            model_name="message",
            name="pending_reception",
        ),
        migrations.RemoveField(
            model_name="room",
            name="group_name",
        ),
        migrations.AddField(
            model_name="message",
            name="voice",
            field=models.FileField(blank=True, null=True, upload_to="voice/"),
        ),
    ]