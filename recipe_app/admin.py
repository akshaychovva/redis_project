from django.contrib import admin
from . import models

admin.site.register(models.Cat_List)
admin.site.register(models.Category)
admin.site.register(models.Recipe)