from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

class User_profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='photo/', null=True,blank=True)
    


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    posted_date = models.DateField(default=datetime.now)
    is_deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')

