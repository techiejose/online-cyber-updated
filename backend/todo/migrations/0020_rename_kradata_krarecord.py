# Generated by Django 3.2.5 on 2021-12-01 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0019_alter_kradata_datesend'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Kradata',
            new_name='Krarecord',
        ),
    ]
