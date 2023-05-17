from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ManyToManyField(User, related_name="usersender")
    receiver = models.ManyToManyField(User, related_name="userreceiver")
    body = models.CharField(max_length=155)
    date = models.DateField()