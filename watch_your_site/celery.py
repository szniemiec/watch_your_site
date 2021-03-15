from __future__ import absolute_import, unicode_literals

import os

import django
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'watch_your_site.settings')
django.setup()

app = Celery('watch_your_site')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
