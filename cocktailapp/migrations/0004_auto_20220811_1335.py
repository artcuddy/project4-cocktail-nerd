# Generated by Django 3.2.15 on 2022-08-11 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktailapp', '0003_auto_20220811_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
