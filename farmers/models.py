from django.db import models
from django.contrib.gis.db import models as gis_models


# Create your models here.
class Cultures(models.Model):
    culture_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.culture_name


class Farmers(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=True, blank=True, default=0)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Seasons(models.Model):
    season_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.season_name


class Plots(models.Model):
    contour = gis_models.PointField(srid=4326)
    farmer = models.ForeignKey(Farmers, on_delete=models.DO_NOTHING)
    culture = models.ForeignKey(Cultures, on_delete=models.DO_NOTHING)
    season = models.ForeignKey(Seasons, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str(self.culture)