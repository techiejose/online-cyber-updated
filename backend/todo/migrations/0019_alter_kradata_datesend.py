# Generated by Django 3.2.5 on 2021-12-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0018_rename_dateposted_kradata_datesend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kradata',
            name='datesend',
            field=models.DateField(null=True),
        ),
    ]
