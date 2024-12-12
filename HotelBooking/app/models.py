from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.

# class Room(models.Model):
#     Room_no = models.IntegerField()
#     Room_type = models.CharField(max_length=10, choices= [('Single', 'Single'),('Double', 'Double'),('Suite', 'Suite'),])
#     AC_Room = models.CharField(max_length=10)
#     Non_AC_Room = models.CharField(max_length=10)
#     Price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
#     Room_available = models.BooleanField(default=True)
#     Room_description = models.TextField(blank=True)

#     def __str__(self):
#         return f"Room {self.Room_no} ({self.Room_type})"


class Room(models.Model):
    Room_no = models.CharField(max_length=10)
    Room_type = models.CharField(max_length=20)
    Room_description = models.TextField()
    Price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    Room_available = models.BooleanField(default=True)  # This seems to represent availability

    def __str__(self):
        return f"Room {self.Room_no} ({self.Room_type})"

class Booking(models.Model):
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Booking_date = models.DateTimeField(auto_now_add=True)
    Check_in = models.DateField()
    Check_out = models.DateField()
    Total_price = models.DecimalField(max_digits=10,decimal_places=2)

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
#         return self.Booking