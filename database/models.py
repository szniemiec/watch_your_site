from django.db import models


class Site(models.Model):
    site_id = models.AutoField(primary_key=True)
    site_url = models.CharField(max_length=200)
    check_interval = models.PositiveIntegerField(default=15)


class CeleryResult(models.Model):
    celery_result_id = models.AutoField(primary_key=True)
    http_code = models.TextField(max_length=30)
    date = models.DateTimeField(auto_now=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
