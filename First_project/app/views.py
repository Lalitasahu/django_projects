
from app.models import *
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import action
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .serializer import  *
from rest_framework import viewsets
from django.core.paginator import Paginator
from datetime import datetime
from django.utils import timezone
import pandas as pd
from decimal import Decimal
import re
from django.db.models import Q, Count
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, generics, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


# Genric view set 
# class CategroyByCategoryViewset(ListAPIView):
#     queryset = sub_cat.objects.all()
#     serializer_class = SubCategoryByCategory

#     def get(self, request, *args, **kwargs):
#         _id = kwargs['id']
#         sub = sub_cat.objects.filter(cat_id = _id)
#         serializer=SubCategoryByCategory(sub,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

class MostOrderedProductsAPIView(APIView):
    def get(self, request):
        most_ordered = (
            Order.objects.values('product')
            .annotate(order_count=Count('id'))
            .order_by('-order_count')[:5]
        )

        product_ids = [item['product'] for item in most_ordered]
        products = Product.objects.filter(id__in=product_ids)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
# class TrendingProductsAPIView(APIView):
#     def get(self, request):
#         delivery_date = timezone.now() - timedelta(days=7)
#         trending = (
#             Order.objects.filter(booking_date=delivery_date)
#             .values('product')
#             .annotate(order_count=Count('id'))
#             .order_by('-order_count')[:10]
#         )
#         product_ids = [item['product'] for item in trending]
#         products = Product.objects.filter(id__in=product_ids)
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

# class TrendingProductsAPIView(APIView):
#     def get(self, request):
#         one_week_ago = timezone.now() - timedelta(days=7)

#         trending = (
#             ProductSearchLog.objects
#             .filter(searched_at__gte=one_week_ago)
#             .values('product')
#             .annotate(search_count=Count('id'))
#             .order_by('-search_count')[:10]
#         )

#         product_ids = [item['product'] for item in trending]
#         products = Product.objects.filter(id__in=product_ids)
#         serializer = ProductSerializer(products, many=True)
        # return Response(serializer.data)

class ProductSearchListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'category_name','price','description'] 

class BuyAllProductsCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        shipping_address = request.data.get("shipping_address")

        cart_items = Cart.objects.filter(user=user)

        if not cart_items.exists():
            return Response({"error": "Your cart is empty!"}, status=status.HTTP_400_BAD_REQUEST)

        order_items = []

        for item in cart_items:
            product = item.product
            quantity = item.quantity

            raw_price = product.price 
            clean_price = Decimal(re.sub(r'[^\d.]', '', str(raw_price)))

            order = Order.objects.create(
                user=user,
                product=product,
                quantity=quantity,
                price=clean_price,
                shipping_address=shipping_address,
                delivery_date=datetime.today().date()
            )

            order_items.append(order)
            order.save()

            # Update product stock
            product.stock -= quantity
            product.is_available = product.stock > 0
            product.save()

        # Clear cart
        cart_items.delete()

        # Serialize
        serializer = BuyAllProductSerializer(order_items, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReviewListView(ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewByProductSerializer

    def get(self, request, *args, **kwargs):
        _id = kwargs['id']
        review = Reviews.objects.filter(product_id=_id)
        serializer = ReviewByProductSerializer(review, many = True)
        return Response (serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = request.user
    profile = request.user.profile
    return Response({
        "user_id":user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone_no": profile.phone_no,
        "address": profile.address,
        "profile_pic": profile.profile_pic.url if profile.profile_pic else None,  
        "is_vendor": profile.is_vendor,
    })


class CategroyByCategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategroyByCategory

    def retrieve(self, request, *args, **kwargs):
        _id = kwargs['pk']
        category = Category.objects.filter(id=_id)
        serializer = CategroyByCategory(category, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class ProductByCategoryViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductByCategory
    
    def retrieve(self, request, *args, **kwargs):
        _id = kwargs['pk']
        product = Product.objects.filter(cat_id=_id)
        serializer = ProductByCategory(product, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        username = request.data.get("username")
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        address = request.data.get('address')
        password = request.data.get('password')
        phone_no = request.data.get('phone_no')
        is_vendor = request.data.get('is_vendor')

        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)  # Securely hash the password
        user.save()

        profile = Profile.objects.create(
            user=user,
            address=address,
            phone_no=phone_no,
            is_vendor=is_vendor,
            # profile_pic=profile_pic
        )
        profile.save()
    
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProfileSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class =  ProfileSerializer

    # def user_profile(request):
    #     user = request.user
    #     profile = user.profile 
    #     serializer = ProfileSerializer(profile)
    #     return Response(serializer.data)

class ImageSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer  

    def create(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        product = Product.objects.get(id=product_id)

        images = request.FILES.getlist('image')  

        uploaded_images = []
        for img in images:
            image_obj = Images.objects.create(product=product, image=img)
            uploaded_images.append(image_obj)

        serializer = ImageSerializer(uploaded_images, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProductSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        data = request.POST       
        prodcut = Product.objects.create(
            title = data['title'],
            user_id = request.user.id )
        
        prodcut.save()
        serializer = ProductSerializer(prodcut)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
            product_id = kwargs['pk']
            user_id = request.user.id

            cart = Cart.objects.filter(
                product_id = product_id,
                user_id = user_id
            )
            product = Product.objects.get(id = product_id)
            # print(cart)
            if cart:
                pser = ProductSerializer(product,data={'is_in_cart':True},partial=True)
                if pser.is_valid():
                    pser.save()
                    # print(pser.data)
                else:
                    print(pser.errors)
            else:
                pser = ProductSerializer(product)
            
            return Response(pser.data,status=status.HTTP_200_OK)

class OrderSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        pro_id = request.data.get("pro_id")
        quantity = int(request.data.get("quantity", 1))
        shipping_address = request.data.get("shipping_address")

        user = request.user
        product = get_object_or_404(Product, id=pro_id)

        if isinstance(product.price, str):
            clean_price = Decimal(re.sub(r"[₹,]", "", product.price))
        else:
            clean_price = product.price

        order = Order.objects.create(
            user=user,
            product=product,
            price=clean_price,
            quantity=quantity,
            shipping_address=shipping_address,
            delivery_date=datetime.today().date(),
        )

        product.stock -= quantity
        product.is_available = product.stock > 0
        product.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data)

    @action(detail=True, methods=["patch"])
    def update_status(self, request, pk=None):
        order = self.get_object()
        status_value = request.data.get("status")
        reason = request.data.get("cancel_reason")
        print("this the reasoon",reason)
        if status_value == "cancelled" and not reason:
            return Response({"error": "Please provide a cancellation reason."}, status=status.HTTP_400_BAD_REQUEST)

        if status_value not in dict(Order.STATUS):
            return Response({"error": "Invalid status."}, status=status.HTTP_400_BAD_REQUEST)

        order.status = status_value
        if status_value == "cancelled":
            order.cancel_reason = reason  # ✅ FIXED HERE
        order.save()

        return Response({"message": f"Order marked as {status_value}."}, status=status.HTTP_200_OK)


class CartSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    pagination_class = PageNumberPagination
    
    # pagination_class = Paginator
    # parser_classes = [JSONParser] 
    
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Cart.objects.filter(user=user)
    #     return Cart.objects.none()

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            cart_items = Cart.objects.filter(user=user)
            serializer = self.get_serializer(cart_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        data = request.data
        product_id = data.get('product')
        quantity = data.get('quantity', 1)
        user = request.user

        if Cart.objects.filter(product_id=product_id, user=user).exists():
            return Response({"detail": "Product already in cart."}, status=status.HTTP_400_BAD_REQUEST)

        product = Product.objects.get(id = product_id)
        cart = Cart.objects.create(
            # data = data,
            product = product,
            quantity = quantity,
            user = user
        )
        cart.save()
        serializer = self.get_serializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CategorySet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        
        name = request.data.get("name")
        image = request.FILES.get("image")
        
        category = Category.objects.create(
            name=name,
            image=image
        )
        category.save()
        
        serializers = CategorySerializer(category)
        return Response(serializers.data,status=status.HTTP_201_CREATED)
       
class ReviewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        product_id = self.request.data.get('product')
        serializer.save(user=self.request.user, product_id=product_id)

# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def buy_all_products(request):
#     user = request.user
#     cart_ids = request.data.get("cart_ids", [])
#     if not cart_ids:
#         return Response({"message": "No cart items provided."}, status=400)
#     cart_items = Cart.objects.filter(id__in=cart_ids, user=user)
#     if not cart_items.exists():
#         return Response({"message": "Cart items not found."}, status=404)
#     for cart in cart_items:
#         Order.objects.create(
#             user=user,
#             product=cart.product,
#             quantity=cart.quantity,
#             order_date=datetime.now(),
#             status="Ordered"
#         )
#         cart.delete()
#     return Response({"message": "All products bought successfully."})

def homepage(request):
    categories = Category.objects.all()
    return render(request, 'homepage.html', {'categories':categories})

def delete_review(request,id):
    reviews = Reviews.objects.get(id=id)
    reviews.delete()
    return HttpResponse('Review Deleted')

def show_reviews(request, product_id):
    product = Product.objects.get(id=product_id)
    reviews = Reviews.objects.filter(product=product)
    paginator = Paginator(reviews, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pro_detail.html', {'page_obj': page_obj, 'product': product})

def edit_review(request,id):
    # product = Product.objects.get(id=id)
    reviews = get_object_or_404(Reviews, id=id)
    if request.method == 'POST':
        reviews.comment = request.POST['comment']
        reviews.rating = request.POST['rating']
        reviews.save()

    return render(request, 'reviewpage.html', {'reviews':reviews})

def add_review(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        comment = request.POST['comment']
        rating = request.POST['rating']

        reviews = Reviews.objects.create(
            comment=comment,
            rating=rating,
            product=product,
            user=request.user,
        )
        reviews.save()
        # return redirect('/product_detail/')
        return HttpResponse('sucessful')
    return render(request, 'reviewpage.html')


def searching(request):
    search = request.GET.get("search", " ")  
    data = Product.objects.none()  

    if search:
        data = Product.objects.filter(Q(title__icontains = search))
        # data = Product.objects.filter(title__icontains = search
        #         ) | Product.objects.filter(description__icontains = search)

        paginator = Paginator(data, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
    return render(request, 'product_list.html', {'data':data, "message":search, 'page_obj':page_obj})

def remove_cart(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return HttpResponseRedirect('/')

def show_cart(request):
    product = Product.objects.all()
    cart = Cart.objects.all()
    return render(request, 'add_cart.html', {'cart':cart,'product':product})

@login_required(login_url='/userlogin')
def add_to_cart(request, id):
    
    product  = Product.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        quantity = data['quantity']
        # total = product.price*quantity

        cart = Cart.objects.create( 
            user = request.user,
            product = product,
            quantity = quantity,
            # date = date,
        )
        cart.save()
        return HttpResponseRedirect('/')
    return render(request, 'confirm_cart.html',{'product':product})

@login_required(login_url='/userlogin')
def confirm_order(request,id):
    order = Order.objects.get(id=id)
    order.status = "Confirmed"
    order.save()
    return HttpResponseRedirect('/')

@login_required(login_url='/userlogin')
def cancel_order(request,id):
    order = Order.objects.get(id=id)
    order.status = "Cancelled"
    order.save()
    return HttpResponseRedirect('/')

@login_required(login_url='/userlogin')
def order_detail(request,id):
    try:
        profile = Profile.objects.get(user=request.user)
        if Profile.is_vendor:
            order = Order.objects.get(id=id)
    except Profile.DoesNotExist:
        return HttpResponseRedirect('/')
    return render(request, 'order_detail.html', {'order':order})

@login_required(login_url='/userlogin')
def order_history(request):
    try:
        profile = Profile.objects.get(user=request.user)
        if Profile.is_vendor:
            order = Order.objects.all()
    except Profile.DoesNotExist:
        return HttpResponseRedirect('/')
    return render(request, 'order_history.html', {'order':order})

@login_required(login_url='/userlogin')
def order_item(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        data = request.POST
        
        quantity = int(data['quantity'])

        raw_price = str(product.price)
        clean_price = re.sub(r'[^\d.]', '', raw_price)

        if quantity > product.stock:
            return render(request, 'order_pro.html', {'product': product,
                                                      'error': 'Quantity exceeds available stock.'})
        order = Order.objects.create(
            user=request.user,
            product=product.title,
            price=clean_price,
            quantity=quantity,
            shipping_address=data['shipping_address'],
            status=data['status']
        )
        order.save()

        # Cart.objects.get(user_id = request.user.id, product_id =  product.id).delete()  need to review this is not working incluede this then order is not work
  
        # Update product stock
        product.stock -= quantity
        product.is_available = product.stock > 0  
        product.save()

        # Redirect to the product detail page
        return HttpResponseRedirect('/')

    return render(request, 'order_pro.html', {'product': product})


def pro_detail(request,id):
    # product = ProductNew.objects.get(id=id)
    product = get_object_or_404(Product, id=id)
    
    is_in_cart = Cart.objects.filter(user=request.user, product=product).exists() if request.user.is_authenticated else False 
    return render(request, 'pro_detail.html', {'product':product})

@login_required(login_url='/userlogin')
def DeleteImage(request, id):
    if request.method == "POST":
        image_ids = request.POST.getlist('image')  
        for _id in image_ids:
            img = get_object_or_404(Images, id=_id)
            img.delete()
        
    return HttpResponseRedirect('/')

@login_required(login_url='/userlogin')
def del_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect('/')

@login_required(login_url='/userlogin')    
def edit_product(request, id):
    product = Product.objects.get(id=id)
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        print(data)
        files = request.FILES.getlist('image')

        product.name = data['name']
        product.price = data['price']
        product.dis_price = data['dis_price']
        product.brand = data['brand']
        product.model = data['model']
        product.storage = data['storage']
        product.stock = data['stock']
        if data.get('is_available') == 'True':
            product.is_available = 1
        else:
            product.is_available = 0

        product.description = data['description']

        product.save()
        for img in files:
            image = Images.objects.create(product=product, image=img) 
            image.save()
        return HttpResponseRedirect('/') 
    
    return render(request, 'add_product.html', {'product': product, 'categories': categories})

def pro_list(request,id):
    # product = ProductNew.objects.filter(cat_id=id)
    product = Product.objects.filter(cat_id=id)
    paginator = Paginator(product, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product_list.html', {'product':product,'category_id':id, 'page_obj':page_obj})

# def pro_list(request,id):#change function name 'sub_cat'
#     return render(request, 'add_sub_cat.html')

@login_required(login_url='/userlogin')
def add_pro_list(request,id):
    if request.method == 'POST':
        data = request.POST
        files = request.FILES.getlist('image')
        product = Product.objects.create(
        # product = ProductNew.objects.create(
            name = data['name'],
            price = data['price'],
            dis_price = data['dis_price'],
            brand = data['brand'],
            model = data['model'],
            storage = data['storage'],
            stock = data['stock'],
            is_available = data['is_available'],
            description = data['description'],
            category_id = id,
            user=request.user
            )
        product.save()
        for img in files:
            image = Images.objects.create(image=img, product=product)
            image.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'add_product.html')
        
@login_required(login_url='/userlogin')        
def del_category(request,id):
    categories = Category.objects.get(id=id)
    categories.delete()
    return HttpResponseRedirect('/')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_det.html', {'categories': categories})

@login_required(login_url='/userlogin')
def edit_category(request,id):
    print(request.POST)
    categories = Category.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        image = request.FILES['image']
        categories.name = data['name']
        categories.image = image
        categories.save()
        return HttpResponseRedirect('/')
    return render(request, 'add_category.html', {'categories':categories})

@login_required(login_url='/userlogin')
def add_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        categories = Category.objects.create(
            name=name,
            image=image)
        categories.save()
        return HttpResponseRedirect('/')
    return render(request, 'add_category.html')

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponse('user and password not valid')
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return render(request,'login.html')

@login_required(login_url='/userlogin')
def createuser(request):
    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        if User.objects.filter(username=data['username']).exists():
            return HttpResponse("Error: Username already exists. Please enter another username.")
        
        user = User.objects.create(
            username = data['username'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email']
        )
        user.set_password(data['password'])
        user.save()

        profile = Profile.objects.create(
            user=user, 
            address = data['address'],
            phone_no = data['phone_no'],
            is_vendor = data['is_vendor'],
            profile_pic = files['profile_pic']
        )
        profile.save()
    return render(request, 'createuser.html')

def userprofile(request):
    return render(request, 'profile.html',{'user':request.user})



def ajax_page(request):
    return render(request,'new_page.html')
    # return render(request,'ajex_page.html')
    # return render(request,'cat_ajax.html')