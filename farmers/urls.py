from django.urls import path
from .views import PlotViewSet, PlotDetViewSet

urlpatterns = [
    path('', PlotViewSet.as_view(), name='plots' ),
    path('details/<int:pk>', PlotDetViewSet.as_view(), name='plot_details' ),
]