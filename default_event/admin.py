from django.contrib import admin
from default_event import models

class EventAdmin (admin.ModelAdmin):
    list_display = ('type','group','site','value')
    search_fields = ('type','site')

class GenericAdmin (admin.ModelAdmin):
    list_display = ('items','value')
    search_fields = ('items',)

class TypeAdmin (admin.ModelAdmin):
    list_display = ('items','value', 'eventType')
    search_fields = ('items', 'eventType')

# Register your models here.
admin.site.register(models.EventType, EventAdmin)
admin.site.register(models.Group)
admin.site.register(models.Catering, TypeAdmin)
admin.site.register(models.Drinks, TypeAdmin)
admin.site.register(models.Site, GenericAdmin)
admin.site.register(models.Music, GenericAdmin)
admin.site.register(models.Entertainment, TypeAdmin)