from django.contrib import admin
from default_event import models

# Register your models here.
admin.site.register(models.EventTipe)
admin.site.register(models.Group)
admin.site.register(models.Banquetry)
admin.site.register(models.Site)
admin.site.register(models.Music)
admin.site.register(models.Entertainment)