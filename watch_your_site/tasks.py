import requests
from celery import Task
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from database.models import Task, Result
from watch_your_site.celery import app


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    for task_object in Task.objects.all():
        task_name = 'fetch ' + task_object.url
        interval_schedule = IntervalSchedule.objects.create(every=task_object.interval,
                                                            period=IntervalSchedule.SECONDS)
        sender.add_periodic_task(task_object.interval, fetch_url.s(task_object.url, task_object.id), name=task_name)
        PeriodicTask.objects.create(interval=interval_schedule, name=task_name,
                                    task='watch_your_site.tasks.fetch_url')


@app.task
def fetch_url(url, task_id):
    http_code = -1
    try:
        http_code = requests.get(url, verify=False, timeout=5).status_code
    except http_code < 0:
        http_code = 'timeout'
    finally:
        Result.objects.create(http_code=http_code, task_id=task_id).save()
