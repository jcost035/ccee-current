# Generated by Django 3.1.5 on 2024-08-06 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0085_auto_20231005_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End Date'),
        ),
    ]
