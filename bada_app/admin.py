from django.contrib import admin
from bada_app import models

class EventAdmin (admin.ModelAdmin):
    readonly_fields = ('search_id', 'created', 'updated')
    list_display = ('state','event_type', 'search_id','created')
    search_fields = ('state', 'event_type')

class CustomerAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'event_booking')
    list_display = ('name', 'last_name','created', 'event_booking')
    search_fields = ('rut', 'email', 'event_booking')    


admin.site.register(models.EventBooking, EventAdmin)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Mailer)




