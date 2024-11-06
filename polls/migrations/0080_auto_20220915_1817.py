# Generated by Django 3.1.5 on 2022-09-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0079_auto_20220815_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='hide_banner',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='pdf',
            field=models.FileField(blank=True, upload_to='programs'),
        ),
    ]
