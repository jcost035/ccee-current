# Generated by Django 3.1.5 on 2021-02-10 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20210210_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='photo',
            field=models.ImageField(default='media/staff-pics/default.jpg', upload_to='media/staff-pics'),
        ),
    ]
