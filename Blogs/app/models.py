from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_admin = models.BooleanField(default=False)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True,blank=True)

    def __str__(self):
        return self.user.username

class Blogs(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    title = models.CharField(max_length=100)
    description = models.TextField()
    datetime = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)
    count_of_comment = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_deate = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.comment_text
    

class Images(models.Model):
    image = models.ImageField(upload_to='photos/')
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE)


class Likes(models.Model):
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # date = models.DateTimeField(auto_now_add=True)

