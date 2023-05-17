from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.CharField(max_length=20)
    trail = models.ForeignKey("Trail", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=155)
    rating = models.IntegerField()
    img = models.CharField(max_length=300)
    date = models.DateField()

