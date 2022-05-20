from django.contrib import admin
from default_event import models

# Register your models here.
admin.site.register(models.EventType)
admin.site.register(models.Group)
admin.site.register(models.Catering)
admin.site.register(models.Drinks)
admin.site.register(models.Site)
admin.site.register(models.Music)
admin.site.register(models.Entertainment)