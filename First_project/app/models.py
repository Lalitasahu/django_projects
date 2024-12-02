from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# from django.utils import timezone
# import django.utils.timezone.now
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    datetime = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) ->str:
        return self.title