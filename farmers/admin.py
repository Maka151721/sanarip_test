from django.contrib import admin
from django.contrib.gis import admin
from .models import Cultures, Farmers, Seasons, Plots

# Register your models here.

@admin.register(Cultures)
class CultureAdmin(admin.ModelAdmin):
    list_display = ('culture_name','description')
    list_filter = ('culture_name', )
    search_fields = ("culture_name__startswith", )

@admin.register(Farmers)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('username','name','age', 'address')
    list_filter = ('name', )
    search_fields = ("name__startswith", )

@admin.register(Plots)
class PlotAdmin(admin.OSMGeoAdmin):
    list_display = ('farmer','culture','season')
    list_filter = ('farmer', 'culture' )
    
    

admin.site.register(Seasons)