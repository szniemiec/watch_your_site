from django.contrib import admin

from .models import Task, Result

admin.site.register([Task, Result])
