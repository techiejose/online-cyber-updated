# Generated by Django 3.2.5 on 2021-10-31 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0013_auto_20210830_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
