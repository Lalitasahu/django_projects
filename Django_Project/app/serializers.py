from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Images
from datetime import datetime


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Product
        fields = '__all__'

class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Images
        # fields = '__all__'
        fields = ('id','Pro_id','Pro_images')

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     id = serializers.ReadOnlyField()
#     class Meta:
#         fields = '__all__'

