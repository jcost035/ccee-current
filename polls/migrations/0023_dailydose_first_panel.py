# Generated by Django 3.1.5 on 2021-05-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_auto_20210526_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailydose',
            name='first_panel',
            field=models.BooleanField(null=True),
        ),
    ]
