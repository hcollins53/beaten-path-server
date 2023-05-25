from django.db import models

class Trail(models.Model):
    name = models.CharField(max_length=155)
    length = models.FloatField()
    elevationGain = models.IntegerField()
    difficulty = models.CharField(max_length=20)
    lat = models.FloatField()
    lon = models.FloatField()
    img = models.CharField(max_length=300)
    permit = models.CharField(max_length=20)
    fees = models.CharField(max_length=155)
