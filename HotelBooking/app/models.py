from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    phone_number = models.CharField(max_length=10)
    is_vendor = models.BooleanField(default=False)
    profile_pic = models.ImageField(null=True,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)


class Room(models.Model):
    Room_no = models.CharField(max_length=10)
    Room_type = models.CharField(max_length=20)
    Room_description = models.TextField()
    Price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    Room_available = models.BooleanField(default=True)  # This seems to represent availability

    def __str__(self):
        return f"Room {self.Room_no} ({self.Room_type})"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Inprocess', 'Inprocess'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Booking_date = models.DateTimeField(auto_now_add=True)
    Check_in = models.DateField()
    Check_out = models.DateField()
    Total_price = models.DecimalField(max_digits=10,decimal_places=2)
    Num_of_Person = models.IntegerField(null=True)

    def __str__(self) ->str:
        return self.user
    
    
# class Payment(models.Model):
#     Booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
#     Payment_method = models.CharField(max_length=20, choices=[('Credit Card', 'Credit Card'),
#         ('Debit Card', 'Debit Card'),('PayPal', 'PayPal'),('Cash', 'Cash'),])
#     Payment_date = models.DateTimeField(auto_now_add=True)
#     Total_amount = models.DecimalField(max_digits=10,decimal_places=2)
#     Payment_status = models.CharField(max_length=20, choices=[('Panding','Panding'),('Complete','Complete'),('Failed','Failed'),])

#     def __str__(self) ->str:
#         return self.Bookingfrom django.db import models
