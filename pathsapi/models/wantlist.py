from django.db import models
from django.contrib.auth.models import User

class Wantlist(models.Model):
    trail = models.ForeignKey("Trail", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)