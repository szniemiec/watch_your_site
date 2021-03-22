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
        sender.add_periodic_task(task_object.interval, fetch_url.s(task_object.id), name=task_name)
        PeriodicTask.objects.create(interval=interval_schedule, name=task_name,
                                    task='watch_your_site.tasks.fetch_url', args=[task_object.id, ])


@app.task
def fetch_url(task_id):
    task = Task.objects.get(pk=task_id)
    http_code = 'timeout'
    try:
        http_code = requests.get(task.url, verify=False, timeout=5).status_code
    except TypeError:
        http_code = 'bad task'
    finally:
        Result.objects.create(http_code=http_code, task_id=task.id).save()
