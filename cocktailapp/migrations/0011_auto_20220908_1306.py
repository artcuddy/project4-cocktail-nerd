# Generated by Django 3.2.15 on 2022-09-08 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocktailapp', '0010_remove_post_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.SET_DEFAULT, to='cocktailapp.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]