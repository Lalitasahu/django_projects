from rest_framework import serializers 
from django.contrib.auth.models import User 
from .models import Blogs, User
from datetime import datetime
  
class BlogsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    datetime = serializers.DateTimeField(default=datetime.now)
    count_of_Like = serializers.IntegerField(default=0)
    count_of_comment = serializers.IntegerField(default=0)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Corrected field?
   
    class Meta:  
        model = Blogs  
        fields = '__all__'
