# Generated by Django 3.2.15 on 2022-08-12 08:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktailapp', '0005_auto_20220812_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='stars',
            field=models.PositiveIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
