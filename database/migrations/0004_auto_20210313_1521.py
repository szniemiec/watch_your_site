# Generated by Django 3.1.7 on 2021-03-13 15:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20210313_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='http_code',
            field=models.TextField(default='method error', max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='url',
            field=models.TextField(default='url error', max_length=200),
        ),
        migrations.AlterField(
            model_name='result',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 13, 15, 21, 45, 520721, tzinfo=utc)),
        ),
    ]