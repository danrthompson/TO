from django.db import models
from profiles.models import Profile

class Event(models.Model):
  name      = models.CharField(max_length=100)
  date      = models.CharField(max_length=100)
  design    = models.BooleanField()
  hacking   = models.BooleanField()
  social    = models.BooleanField()
  creator   = models.ForeignKey(Profile)
