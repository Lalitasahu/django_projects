from rest_framework import serializers 
from django.contrib.auth.models import User 
from .models import Room, User, Booking
from datetime import datetime


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        # fields = ('id','Room_no','Room_type','url','Room_description','')
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


# class ProfileS