# Generated by Django 3.2.14 on 2022-10-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0009_payhistory_authority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payhistory',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]