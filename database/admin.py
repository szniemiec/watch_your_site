from django.contrib import admin
from .models import Site, CeleryResult

admin.site.register([Site, CeleryResult])