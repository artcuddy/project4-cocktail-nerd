# Generated by Django 3.2.15 on 2022-09-14 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktailapp', '0027_auto_20220914_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]