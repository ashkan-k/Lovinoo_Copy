# Generated by Django 3.2.14 on 2022-10-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='سن'),
        ),
    ]