from rest_framework import serializers
from SocialMediaApp.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'username', 'email', 'first_name', 'last_name']
        fields = "__all__"

class SnapUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnapUser
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
