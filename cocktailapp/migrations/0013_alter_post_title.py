# Generated by Django 3.2.15 on 2022-09-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktailapp', '0012_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
