# Generated by Django 4.1 on 2022-08-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0003_profile_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="confirmed_image",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="profile",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
