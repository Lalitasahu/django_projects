from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    address = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    is_vendor = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='photos/',  blank=True, null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/',null=True)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True )
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/',null=True)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dis_price = models.DecimalField(max_digits=10,decimal_places=2)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    storage = models.CharField(max_length=20)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Order(models.Model):
    STATUS = [
    ('pending', 'pending'),
    ('confirmed', 'confirmed'),
    ('cancelled', 'cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='Cancelled')
    shipping_address = models.TextField()

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='photos/')
    upload_date = models.DateTimeField(auto_now_add=True)

    