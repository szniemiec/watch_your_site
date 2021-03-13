from django.contrib import admin

from .models import Interval, Task

admin.site.register([Interval, Task])
