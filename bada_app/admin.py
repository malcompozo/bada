from django.contrib import admin
from bada_app import models

class EventAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'search_id')
    list_display = ('state', 'site','created')
    search_fields = ('state', 'site')

class CustomerAdmin (admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('name', 'last_name','created')
    search_fields = ('rut', 'email')    


admin.site.register(models.EventBooking, EventAdmin)
admin.site.register(models.Customer, CustomerAdmin)



