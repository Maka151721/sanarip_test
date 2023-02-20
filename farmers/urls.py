from django.urls import path
from .views import PlotViewSet

urlpatterns = [
    path('', PlotViewSet.as_view(), name='plots' ),
]