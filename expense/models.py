from django.db import models

# Create your models here.

class Features(models.Model):
   Name = models.CharField(max_length=250)
   details = models.CharField(max_length=250)
