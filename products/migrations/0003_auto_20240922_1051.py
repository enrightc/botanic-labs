# Generated by Django 3.2.25 on 2024-09-22 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20240922_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='recommendations',
        ),
        migrations.AddField(
            model_name='product',
            name='recommendation_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_recommendation', to='products.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='recommendation_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_recommendation', to='products.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='recommendation_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='third_recommendation', to='products.product'),
        ),
    ]
