# Generated by Django 3.2.15 on 2022-09-09 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktailapp', '0018_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
    ]