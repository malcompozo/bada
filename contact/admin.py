from django.contrib import admin
from contact import models

class ContactAdmin (admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('name', 'email', 'created')
    search_fields = ('name', 'email')

    
admin.site.register(models.Contact, ContactAdmin)