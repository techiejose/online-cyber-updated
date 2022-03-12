# Generated by Django 3.2.5 on 2021-12-01 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0020_rename_kradata_krarecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Krarecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=120, null=True)),
                ('profession', models.CharField(max_length=120)),
                ('idno', models.IntegerField(max_length=20, null=True)),
                ('dob', models.DateField(null=True)),
                ('box', models.CharField(max_length=120, null=True)),
                ('county', models.CharField(max_length=120, null=True)),
                ('town', models.CharField(max_length=20, null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('datesend', models.DateField(null=True)),
                ('mobile2', models.IntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Krarecord',
        ),
    ]