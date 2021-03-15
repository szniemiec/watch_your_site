from django.db import models

from django.utils.timezone import now


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.TextField(max_length=200, default='url error')
    interval = models.PositiveIntegerField(default=15)


class Result(models.Model):
    id = models.AutoField(primary_key=True)
    http_code = models.TextField(max_length=200, default='method error')
    date = models.DateTimeField(default=now())

# class Interval(models.Model):
#     id = models.AutoField(primary_key=True)
#     interval = models.PositiveIntegerField(default=15)
