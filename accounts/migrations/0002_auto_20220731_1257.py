# Generated by Django 3.2.13 on 2022-07-31 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="otpcode",
            options={},
        ),
        migrations.RemoveField(
            model_name="otpcode",
            name="modified",
        ),
        migrations.AlterField(
            model_name="otpcode",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
