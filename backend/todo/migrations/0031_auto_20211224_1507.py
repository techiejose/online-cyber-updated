# Generated by Django 3.2.5 on 2021-12-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0030_auto_20211224_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='about',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
