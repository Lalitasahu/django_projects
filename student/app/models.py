from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    # name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) ->str:
        return self.title