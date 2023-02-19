from django.contrib import admin
from django.contrib.gis import admin
from .models import Cultures, Farmers, Seasons, Plots

# Register your models here.

admin.site.register(Cultures)
admin.site.register(Farmers)

@admin.register(Plots)
class PlotAdmin(admin.OSMGeoAdmin):
    pass
    

admin.site.register(Seasons)