from django.db import models

from django.utils.timezone import now


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.TextField(max_length=200, default='url error')
    interval = models.PositiveIntegerField(default=15)

    def __str__(self):
        str = self.id + ',' + self.url + ',' + self.interval
        return str


class Result(models.Model):
    id = models.AutoField(primary_key=True)
    http_code = models.TextField(max_length=200, default='method error')
    date = models.DateTimeField(default=now())
    task_id = models.PositiveIntegerField(default=0)

    def __str__(self):
        str = self.id + ',' + self.http_code + ',' + self.date + ',' + self.task_id
        return str
