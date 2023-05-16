from django.db import models

class Trail(models.Model):
    name = models.CharField(max_length=155)
    length = models.IntegerField()
    elevationGain = models.IntegerField()
    difficulty = models.CharField(max_length=20)
    lat = models.IntegerField()
    lon = models.IntegerField()
    img = models.CharField(max_length=300)
    permit = models.CharField(max_length=20)
    fees = models.CharField(max_length=155)
