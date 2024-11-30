from django.db import models
from datetime import datetime

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    
    
    def __str__(self) ->str:
        return self.title