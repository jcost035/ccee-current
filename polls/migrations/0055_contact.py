# Generated by Django 3.1.5 on 2021-06-18 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0054_auto_20210616_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.CharField(blank=True, default='', max_length=200)),
                ('content', models.CharField(blank=True, default='', max_length=10000)),
            ],
        ),
    ]