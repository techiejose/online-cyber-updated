# Generated by Django 3.2.5 on 2021-08-17 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20210806_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('author', models.CharField(max_length=120, null=True)),
                ('dateposted', models.DateField(null=True)),
            ],
        ),
    ]