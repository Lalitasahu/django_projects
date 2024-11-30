from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    posted_date = models.DateField(default=datetime.now)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.Title




# from django.db import models
# from datetime import datetime

# class Product(models.Model):
#     CATEGORY_CHOICES = [
#         ('laptop', 'Laptop'),
#         ('stationery', 'Stationery'),
#         ('toys', 'Toys'),
#     ]
#     title = models.CharField(max_length=50)
#     price = models.FloatField()
#     description = models.TextField()
#     posted_date = models.DateField(default=datetime.now)
    # category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=True)
#     is_deleted = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title
