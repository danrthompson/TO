from django.db import models

class Profile(models.Model):
  name          = models.CharField(max_length=100)
  password      = models.CharField(max_length=100)
  email         = models.CharField(max_length=100)
  design        = models.BooleanField()
  have_css      = models.BooleanField()
  have_php      = models.BooleanField()
  want_css      = models.BooleanField()
  want_php      = models.BooleanField()
  date_created  = models.DateTimeField()
