from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework import generics
from .models import Plots
from .serializers import PlotSerializer

# Create your views here.
class PlotViewSet(generics.ListAPIView):
    queryset = Plots.objects.all()
    serializer_class = PlotSerializer

    def get_queryset(self):
        queryset = super().get_queryset().filter(farmer=self.request.user)
        return queryset

class PlotDetViewSet(generics.RetrieveUpdateAPIView):
    queryset = Plots.objects.all()
    serializer_class = PlotSerializer


