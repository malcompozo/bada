from django.contrib import admin
from bada_app import models

class EventAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'search_id')
    list_display = ('event_type', 'search_id','created')
    search_fields = ('event_type', 'search_id')

class CustomerAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'event_booking')
    list_display = ('name', 'last_name','created', 'event_booking')
    search_fields = ('rut', 'email', 'event_booking')    


admin.site.register(models.EventBooking, EventAdmin)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Mailer)




