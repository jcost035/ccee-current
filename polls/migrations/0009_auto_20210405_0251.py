# Generated by Django 3.1.5 on 2021-04-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='grade_level',
            field=models.CharField(choices=[('K', 'K-12'), ('E', 'Educator')], default='K', max_length=2),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='Virtual', max_length=200),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.CharField(default='', max_length=200),
        ),
    ]
