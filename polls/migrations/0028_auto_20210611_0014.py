# Generated by Django 3.1.5 on 2021-06-11 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_news_thumb_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='location',
        ),
        migrations.AddField(
            model_name='news',
            name='content',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
