# Generated by Django 3.1.4 on 2020-12-27 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoonblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default="Yoon's Blog", max_length=255),
        ),
    ]
