# Generated by Django 3.1.5 on 2021-03-23 02:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20210210_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('description', models.CharField(max_length=1200)),
            ],
        ),
    ]
