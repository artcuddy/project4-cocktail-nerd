# Generated by Django 3.2.15 on 2022-09-26 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktailapp', '0036_alter_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
