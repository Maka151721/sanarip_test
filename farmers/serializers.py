from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Plots, Cultures,Farmers


class CultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultures
        fields = ('culture_name',)

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmers
        fields = ('username',)


class PlotSerializer(GeoFeatureModelSerializer):
    culture = CultureSerializer()

    class Meta:
        model = Plots
        geo_field = 'contour'
        fields = ['id','contour', 'culture']