from rest_framework import serializers 
from django.contrib.auth.models import User 
from .models import Blogs, User, Likes
from datetime import datetime
  
# class BlogsSerializer(serializers.ModelSerializer):
#     title = serializers.CharField(max_length=100)
#     description = serializers.CharField()
#     datetime = serializers.DateTimeField(default=datetime.now)
#     count_of_Like = serializers.IntegerField(default=0)
#     count_of_comment = serializers.IntegerField(default=0)
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
   
#     class Meta:  
#         model = Blogs  
#         fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','username')


class BlogsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:  
        model = Blogs  
        fields = '__all__'




class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'
