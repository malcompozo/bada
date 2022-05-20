from django.contrib import admin
from slider import models

class SliderAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'created_at')

# Register your models here.
admin.site.register(models.Slider, SliderAdmin)