# Generated by Django 3.1.5 on 2021-07-26 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0059_auto_20210726_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailydose',
            name='second_video_path',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
