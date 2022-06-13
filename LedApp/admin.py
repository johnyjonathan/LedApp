from atexit import register
from django.contrib import admin
from LedApp import models

admin.site.register(models.settings)
