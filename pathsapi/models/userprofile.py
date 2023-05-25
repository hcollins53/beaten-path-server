from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
    favorite_hike = models.CharField(max_length=20)
    description = models.CharField(max_length=155)
    area = models.CharField(max_length=50)
