from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ManyToManyField(User, on_delete=models.DO_NOTHING, related_name="usermessages")
    receiver = models.ManyToManyField(User, on_delete=models.DO_NOTHING, related_name="usermessages")
    body = models.CharField(max_length=155)
    date = models.DateField()