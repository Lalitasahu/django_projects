from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    datetime = models.DateTimeField(default=datetime.now())
    # user = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self) ->str:
        return self.title