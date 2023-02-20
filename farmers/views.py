from django.shortcuts import render
from rest_framework import generics
from .models import Plots
from .serializers import PlotSerializer

# Create your views here.
class PlotViewSet(generics.ListCreateAPIView):
    queryset = Plots.objects.all()
    serializer_class = PlotSerializer