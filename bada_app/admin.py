from django.contrib import admin
from bada_app import models

class ContactAdmin (admin.ModelAdmin):
    readonly_fields = ('fecha',)
    list_display = ('name', 'email', 'fecha')
    #ordering = ('name',)
    search_fields = ('name', 'email')

class EventAdmin (admin.ModelAdmin):
    readonly_fields = ('fecha',)
    list_display = ('estado', 'recinto','fecha')
    search_fields = ('estado', 'recinto')

admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.Estado_evento, EventAdmin)
