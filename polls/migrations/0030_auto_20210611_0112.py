# Generated by Django 3.1.5 on 2021-06-11 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0029_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='external',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='external_url',
            field=models.CharField(blank=True, max_length=1200, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.CharField(blank=True, max_length=1200, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='tags',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
