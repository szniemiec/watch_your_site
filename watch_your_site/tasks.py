import datetime

from celery.worker.state import requests

from database.models import Site, CeleryResult
from watch_your_site.celery import app


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sites = Site.objects.all()
    print('loaded sites')
    for site in sites:
        site_url = site.site_url
        check_interval = site.check_interval
        sender.add_periodic_task(check_interval, fetch_url(site),
                                 name='Task for ' + site_url + ' | Interval: ' + check_interval)


@app.task
def fetch_url(site):
    print('fetching')
    http_code = requests.get(site.site_url).status_code
    print(http_code)
    celery_result = CeleryResult(http_code=http_code, date=datetime.datetime.now(), site=site.site_id)
    CeleryResult.save(celery_result)
