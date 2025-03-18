
from app.models import *
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .serializer import  *
from rest_framework import viewsets
from django.core.paginator import Paginator
from datetime import datetime
import pandas as pd
import re
from django.db.models import Q

class UserSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class =  ProfileSerializer

class ProductSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        pro_id = request.data.get("pro_id")
        product = Product.objects.get(id=pro_id)
        quantity = request.data.get("quantity", 1) 
        shipping_address = request.data.get("shipping_address")
        user_id = request.data.get('user_id')
        # delivery_date = request.data.get("delivery_date")
        # print(request.data)

        order = Order.objects.create(
            product = product.name,
            price = product.price,
            quantity = quantity,
            shipping_address = shipping_address,
            delivery_date = datetime.today().date(),
            user_id = user_id
        )
        order.save()
    
        product.stock -= quantity
        product.is_available = product.stock > 0
        product.save()
        
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class CartSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CategorySet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


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
        #         ) | Product.objects.filter(brand__icontains = search
        #         ) | Product.objects.filter(model__icontains = search
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

        Cart.objects.get(user_id = request.user.id, product_id =  product.id).delete()
  
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