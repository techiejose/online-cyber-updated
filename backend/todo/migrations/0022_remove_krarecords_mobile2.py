# Generated by Django 3.2.5 on 2021-12-01 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0021_auto_20211201_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='krarecords',
            name='mobile2',
        ),
    ]