# Generated by Django 3.1.5 on 2024-08-09 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0088_auto_20240809_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
