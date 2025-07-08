from rest_framework import serializers 
from django.contrib.auth.models import User 
from .models import *
from datetime import datetime

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Profile
        fields = ('address','phone_no','is_vendor')

class ReviewsSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Reviews
        fields = ['id', 'product', 'user','user_name' ,'comment', 'rating', 'created_at']
        read_only_fields = ['user', 'created_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    user_id = serializers.ReadOnlyField(source = "user.id")
    is_in_cart = serializers.BooleanField(default=False)
    category = serializers.CharField(source='cat.title', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    cancellation_reason = serializers.CharField(source='cancel_reason', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        # fields = ('id','product','price','quantity','booking_date','delivery_date','shipping_address')

class BuyAllProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Cart
        fields = '__all__'
        # fields = ('id', 'product','quantity','data' )
        # read_only_fields = ('user','date') 


class CategroyByCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductByCategory(serializers.ModelSerializer):
    # images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = "__all__"
        # fields = ['id','title','image_list','model_name','cat']


# class ReviewByProduct(generics.RetrieveUpdateDestroyAPIView):
class ReviewByProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"