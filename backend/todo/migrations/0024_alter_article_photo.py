# Generated by Django 3.2.5 on 2021-12-09 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0023_krarecords_datecompleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
