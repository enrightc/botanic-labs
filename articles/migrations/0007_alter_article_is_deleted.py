# flake8: noqa
# Generated by Django 3.2.25 on 2024-09-29 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Mark as hidden'),
        ),
    ]
