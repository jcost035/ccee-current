# Generated by Django 3.1.5 on 2021-06-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0032_event_thumb_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='thumb_photo',
            field=models.ImageField(blank=True, default='', upload_to='programs'),
        ),
        migrations.AlterField(
            model_name='news',
            name='thumb_photo',
            field=models.ImageField(blank=True, default='', upload_to='programs'),
        ),
    ]
