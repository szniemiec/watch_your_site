from django.contrib import admin

from .models import Task, Result


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', 'interval']


class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'http_code', 'date', 'task_id']


admin.site.register(Task, TaskAdmin)

admin.site.register(Result, ResultAdmin)
