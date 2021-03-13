from django.db import models


class Interval(models.Model):
    id = models.AutoField(primary_key=True)
    interval = models.PositiveIntegerField(default=15)


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.TextField
    interval = models.ForeignKey(Interval, on_delete=models.CASCADE)
