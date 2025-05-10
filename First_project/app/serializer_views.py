
# from app.models import *
# from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from rest_framework.views import APIView  
# from rest_framework.response import Response  
# from rest_framework import status  
# from .serializer import  *
# from rest_framework import viewsets
# from django.core.paginator import Paginator
# from datetime import datetime
# import pandas as pd
# import re
# from django.db.models import Q
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import AllowAny
# from rest_framework.generics import ListAPIView
# from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions


# # Genric view set 
# # class CategroyByCategoryViewset(ListAPIView):
# #     queryset = sub_cat.objects.all()
# #     serializer_class = SubCategoryByCategory

# #     def get(self, request, *args, **kwargs):
# #         _id = kwargs['id']
# #         sub = sub_cat.objects.filter(cat_id = _id)
# #         serializer=SubCategoryByCategory(sub,many=True)
# #         return Response(serializer.data,status=status.HTTP_200_OK)

# class CategroyByCategoryViewset(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategroyByCategory

#     def retrieve(self, request, *args, **kwargs):
#         _id = kwargs['pk']
#         category = Category.objects.filter(id=_id)
#         serializer = CategroyByCategory(category, many = True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
# class ProductByCategoryViewset(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductByCategory
    
#     def retrieve(self, request, *args, **kwargs):
#         _id = kwargs['pk']
#         product = Product.objects.filter(cat_id=_id)
#         serializer = ProductByCategory(product, many = True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    

# class UserSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.AllowAny,)

#     def create(self, request, *args, **kwargs):
#         username = request.data.get("username")
#         first_name = request.data.get('first_name')
#         last_name = request.data.get('last_name')
#         email = request.data.get('email')
#         address = request.data.get('address')
#         password = request.data.get('password')
#         phone_no = request.data.get('phone_no')
#         is_vendor = request.data.get('is_vendor')

#         user = User.objects.create(
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#             email=email
#         )
#         user.set_password(password)  # Securely hash the password
#         user.save()

#         profile = Profile.objects.create(
#             user=user,
#             address=address,
#             phone_no=phone_no,
#             is_vendor=is_vendor,
#             # profile_pic=profile_pic
#         )

#         profile.save()
        
    
#         # serializer = self.get_serializer( user, context={'request': request})

#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# #     def create(self,request, *args, **kwargs):
# #         username = request.data.get("username")
# #         password = request.data.get("password")
# #         if not username or not password:
# #             return Response(
# #                 {"detail": "Username and password are required."},
# #                 status=status.HTTP_400_BAD_REQUEST
# #             ) 
# #         user = authenticate(request, username=username, password=password)
# #         if not user:
# #             return Response(
# #                 {"detail": "Invalid credentials."},
# #                 status=status.HTTP_401_UNAUTHORIZED
# #             )
# #         refresh = RefreshToken.for_user(user)
# #         access_token = str(refresh.access_token)
# #         return Response({
# #             "access": access_token,
# #             "refresh": str(refresh),
# #         }, status=status.HTTP_200_OK)
    


# class ProfileSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class =  ProfileSerializer


#     # def user_profile(request):
#     #     user = request.user
#     #     profile = user.profile 
#     #     serializer = ProfileSerializer(profile)
#     #     return Response(serializer.data)

# class ImageSet(viewsets.ModelViewSet):
#     queryset = Images.objects.all()
#     serializer_class = ImageSerializer  

#     def create(self, request, *args, **kwargs):
#         product_id = request.data.get('product_id')
#         product = Product.objects.get(id=product_id)

#         images = request.FILES.getlist('image')  

#         uploaded_images = []
#         for img in images:
#             image_obj = Images.objects.create(product=product, image=img)
#             uploaded_images.append(image_obj)

#         serializer = ImageSerializer(uploaded_images, many=True)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class ProductSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class OrderSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     def create(self, request, *args, **kwargs):
#         pro_id = request.data.get("pro_id")
#         product = Product.objects.get(id=pro_id)
#         quantity = request.data.get("quantity", 1) 
#         shipping_address = request.data.get("shipping_address")
#         user_id = request.data.get('user_id')
#         # delivery_date = request.data.get("delivery_date")
#         # print(request.data)

#         order = Order.objects.create(
#             product = product.name,
#             price = product.price,
#             quantity = quantity,
#             shipping_address = shipping_address,
#             delivery_date = datetime.today().date(),
#             user_id = user_id
#         )
#         order.save()
    
#         product.stock -= quantity
#         product.is_available = product.stock > 0
#         product.save()
        
#         serializer = OrderSerializer(order)
#         return Response(serializer.data)

# class CartSet(viewsets.ModelViewSet):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

# class CategorySet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

#     def create(self, request, *args, **kwargs):
        
#         name = request.data.get("name")
#         image = request.FILES.get("image")
        
#         category = Category.objects.create(
#             name=name,
#             image=image
#         )
#         category.save()
        
#         serializers = CategorySerializer(category)
#         return Response(serializers.data,status=status.HTTP_201_CREATED)
    

# class ReviewSet(viewsets.ModelViewSet):
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewsSerializer

#     # def create(self, request, *args, **kwargs):
#         # comment = request.data['comment']
#         # rating = request.data['rating']
#         # product_id = request.data.get('product_id', None)
        
#         # print(comment,rating)
#         # review = Reviews.objects.create(
#         #         user_id = 1,
#         #         comment = comment,
#         #         rating = rating,
#         #         product_id = product_id
#         # )
#         # review.save()

#         # s = ReviewsSerializer(review)
#         # return Response(s.data, status=status.HTTP_201_CREATED)
#     def create(self, request, *args, **kwargs):
#         # print("Received Data:", request.data)

#         product_id = request.data.get('product_id')
#         comment = request.data.get('comment')
#         rating = request.data.get('rating')

#         # print(comment,rating,product_id)
        
#         review = Reviews.objects.create(
#             user_id=3,
#             comment=comment,
#             rating=rating,
#             product_id=product_id
#         )
#         review.save()

#         serializer = ReviewsSerializer(review)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
