from django.db import models
from django.contrib.auth.models import User    

# Create your models here.
class SnapUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=150, unique=True)
    # email = models.EmailField(unique=True)
    # password = models.CharField(max_length=128)
    address = models.CharField(max_length=100, null=True,blank=True)
    phone_no = models.CharField(max_length=15, null=True,blank=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures/', null=True, blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts/images/', null=True, blank=True)
    video = models.FileField(upload_to='posts/videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)