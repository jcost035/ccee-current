# Generated by Django 3.1.5 on 2021-10-13 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0073_auto_20210727_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='registration_url',
            field=models.CharField(blank=True, max_length=1200),
        ),
    ]