import datetime

import requests
from django_celery_beat.models import IntervalSchedule

from database.models import Site, CeleryResult
from watch_your_site.celery import app


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    for site in Site.objects.all():
        check_interval = site.check_interval
        schedule = IntervalSchedule.objects.create(every=check_interval, period=IntervalSchedule.SECONDS)
        sender.add_periodic_task(schedule, fetch_url.s(site.site_url),
                                 name=site.site_url)


@app.task
def fetch_url(url):
    http_code = requests.get(url).status_code
    site = Site.objects.get(url)
    celery_result = CeleryResult(http_code=http_code, date=datetime.datetime.now(), site=site.site_id)
    CeleryResult.save(celery_result)
