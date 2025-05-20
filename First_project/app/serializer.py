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

# class ReviewsSerializer(serializers.Serializer):
#     comment = serializers.CharField(max_length=200)
#     rating = serializers.IntegerField()
#     product_id = serializers.IntegerField()
#     user_id = serializers.IntegerField()
#     created_at = serializers.DateTimeField()

class ReviewsSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Reviews
        fields = ['id', 'product', 'user','user_name' ,'comment', 'rating', 'created_at']
        read_only_fields = ['user', 'created_at']

# class ReviewsSerializer(serializers.ModelSerializer):
#     comment = serializers.CharField(max_length=200)  

#     class Meta:
#         model = Reviews
#         fields = '__all__'

        # fields = ('id','rating','comment','created_at')

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    user_id = serializers.ReadOnlyField(source = "user.id")
    is_in_cart = serializers.BooleanField(default=False)

    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    # name_ = serializers.ReadOnlyField(source="product.product")
    class Meta:
        model = Order
        fields = ('id','product','price','quantity','booking_date','delivery_date','shipping_address')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ('user','date') 

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


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
