# flake8: noqa
# Generated by Django 3.2.25 on 2024-10-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_article_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(max_length=50000),
        ),
    ]
