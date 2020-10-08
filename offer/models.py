from django.db import models

# Create your models here.
class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    discount = models.FloatField()