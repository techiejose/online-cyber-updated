# Generated by Django 3.2.5 on 2021-12-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0025_alter_article_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='krarecords',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
