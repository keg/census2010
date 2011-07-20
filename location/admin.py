from django.contrib import admin
from location.models import State, County, City

class StateAdmin(admin.ModelAdmin):
     prepopulated_fields = {
        'slug': ('name',)
    }

class CountyAdmin(admin.ModelAdmin):
     prepopulated_fields = {
        'slug': ('name',)
    }

admin.site.register(State, StateAdmin)
admin.site.register(County, CountyAdmin)