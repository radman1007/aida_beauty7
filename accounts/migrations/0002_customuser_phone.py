# Generated by Django 5.0.6 on 2024-07-15 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]
