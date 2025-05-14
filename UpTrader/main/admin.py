from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name','menu_name','parent','get_url','order')
    list_filter = ('menu_name',)
    search_fields = ('name', 'url', 'named_url')
    
    def get_url(self, obj):
        return obj.get_url
    get_url.short_description = 'URL'
    