from django.db import models
from datetime import datetime

# Create your models here.


class Phones(models.Model):
    brand = models.CharField(max_length=20)
    storage = models.CharField(max_length=50)
    camera = models.CharField(max_length=20)
    battery = models.CharField(max_length=20)
    display = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) ->str:
        return self.title