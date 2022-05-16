from django.contrib import admin
from bada_app import models

class ContactAdmin (admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('name', 'email', 'created')
    search_fields = ('name', 'email')

class EventAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'search_id')
    list_display = ('state', 'site','created')
    search_fields = ('state', 'site')

class CustomerAdmin (admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('name', 'last_name','created')
    search_fields = ('rut', 'email')    



admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.EventBooking, EventAdmin)
admin.site.register(models.Customer, CustomerAdmin)

admin.site.register(models.EventTipe)
admin.site.register(models.Banquetry)
admin.site.register(models.Site)
admin.site.register(models.Music)
admin.site.register(models.Toys)


