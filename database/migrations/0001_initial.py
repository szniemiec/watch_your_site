# Generated by Django 3.1.7 on 2021-03-23 10:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('http_code', models.TextField(default='method error', max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 3, 23, 10, 20, 56, 575839, tzinfo=utc))),
                ('task_id', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.TextField(default='url error', max_length=200)),
                ('interval', models.PositiveIntegerField(default=15)),
            ],
        ),
    ]
