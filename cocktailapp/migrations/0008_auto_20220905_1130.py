# Generated by Django 3.2.15 on 2022-09-05 11:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktailapp', '0007_auto_20220818_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='stars',
            field=models.PositiveIntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
