# Generated by Django 3.1.5 on 2021-07-26 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0060_dailydose_second_video_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailydose',
            old_name='first_panel_image',
            new_name='first_panel_is_image',
        ),
        migrations.RenameField(
            model_name='dailydose',
            old_name='second_panel_image',
            new_name='second_panel_is_image',
        ),
    ]
