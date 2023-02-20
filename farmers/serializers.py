from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Plots, Cultures


class CultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultures
        fields = ('culture_name',)


class PlotSerializer(GeoFeatureModelSerializer):
    culture = CultureSerializer()

    class Meta:
        model = Plots
        geo_field = 'contour'
        fields = ['contour', 'culture']