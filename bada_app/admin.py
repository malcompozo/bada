from django.contrib import admin
from bada_app import models

class EventAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('state','event_type', 'search_id','created')
    search_fields = ('state', 'event_type')

class CustomerAdmin (admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('name', 'last_name','created')
    search_fields = ('rut', 'email')    


admin.site.register(models.EventBooking, EventAdmin)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Catering)
admin.site.register(models.Drinks)
admin.site.register(models.Site)
admin.site.register(models.Music)
admin.site.register(models.Entertainment)




