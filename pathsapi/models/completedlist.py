from django.db import models
from django.contrib.auth.models import User

class Completedlist(models.Model):
    trail = models.ForeignKey("Trail", on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateField()