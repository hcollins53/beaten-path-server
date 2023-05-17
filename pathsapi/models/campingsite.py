from django.db import models

class CampingSite(models.Model):
    name = models.CharField(max_length=100)
    trail = models.ForeignKey("Trail", on_delete=models.SET_NULL, null=True)
    distance = models.CharField(max_length=50)
    fees = models.CharField(max_length=20)
    site = models.CharField(max_length=200)