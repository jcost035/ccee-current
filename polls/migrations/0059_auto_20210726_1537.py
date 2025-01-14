# Generated by Django 3.1.5 on 2021-07-26 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0058_auto_20210726_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailydose',
            name='first_panel_image',
            field=models.BooleanField(blank=True, default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dailydose',
            name='second_image',
            field=models.ImageField(blank=True, default='', upload_to='programs'),
        ),
        migrations.AlterField(
            model_name='dailydose',
            name='second_panel_image',
            field=models.BooleanField(blank=True),
        ),
    ]
