from django.db import models
from datetime import datetime

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message =  models.TextField()
    Date_Time = models.DateTimeField(default=datetime.now())


    def __str__(self) ->str:
        return self.title