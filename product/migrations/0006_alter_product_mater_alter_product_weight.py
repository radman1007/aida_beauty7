# Generated by Django 5.0.6 on 2024-08-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mater',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
