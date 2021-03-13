import datetime

import requests
from django_celery_beat.models import IntervalSchedule

from database.models import Site, CeleryResult
from watch_your_site.celery import app


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sites = Site.objects.all()
    for site in sites:
        site_url = site.site_url
        check_interval = site.check_interval
        schedule = IntervalSchedule.objects.create(every=check_interval, period=IntervalSchedule.SECONDS)
        sender.add_periodic_task(interval=schedule, task='tasks.fetch_url',
                                 name='Task for ' + site_url + ' | Interval: ' + check_interval)


@app.task
def fetch_url(site):
    http_code = requests.get(site.site_url).status_code
    celery_result = CeleryResult(http_code=http_code, date=datetime.datetime.now(), site=site.site_id)
    CeleryResult.save(celery_result)
