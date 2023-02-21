from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import User


# Create your models here.
class Cultures(models.Model):
    culture_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.culture_name
    
    class Meta:
        verbose_name = 'Culture'
        verbose_name_plural = 'Cultures'


class Farmers(models.Model):
    username = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, default=0)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.username)
    
    class Meta:
        verbose_name = 'Farmere'
        verbose_name_plural = 'Farmers'


class Seasons(models.Model):
    season_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.season_name
    
    class Meta:
        verbose_name = 'Season'
        verbose_name_plural = 'Seasons'


class Plots(models.Model):
    contour = gis_models.PointField(srid=4326)
    farmer = models.ForeignKey(User,on_delete=models.DO_NOTHING, null=True)
    culture = models.ForeignKey(Cultures, on_delete=models.DO_NOTHING)
    season = models.ForeignKey(Seasons, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str(self.culture)
    
    class Meta:
        verbose_name = 'Plot'
        verbose_name_plural = 'Plots'