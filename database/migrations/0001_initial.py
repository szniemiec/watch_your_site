# Generated by Django 3.1.7 on 2021-03-12 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('site_id', models.AutoField(primary_key=True, serialize=False)),
                ('site_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CeleryResult',
            fields=[
                ('celery_result_id', models.AutoField(primary_key=True, serialize=False)),
                ('http_code', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now=True)),
                ('site_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.site')),
            ],
        ),
    ]
