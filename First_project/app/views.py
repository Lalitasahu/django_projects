
from app.models import Profile, Product, Order, Images, Category
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
# from .serializers import  UserSerializer, LikeSerializer
from rest_framework import viewsets

def homepage(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories':categories})

def del_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect('/')
    
def pro_list(request):
    product = Product.objects.all()
    return render(request, 'product_list.html', {'product':product})

def edit_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        product.name = data['name'],
        product.price = data['price'],
        product.dis_price = data['dis_price'],
        product.brand = data['brand'],
        product.model = data['model'],
        product.storage = data['storage'],
        product.stock = data['stock'],
        product.is_available = data['is_available'],
        product.description = data['description'],
        product.category = data['category'],
        
        product.save()
        return HttpResponseRedirect('product_list')# Redirect to a list or detail page after editing

    return render(request, 'add_product.html', {'product':product})

def add_pro_list(request):
    print(request.POST)
    if request.method == 'POST':
        data = request.POST
        files = request.FILES.getlist('image')
        category_name = data.get('category')  # Get the category name from the form
        
        category,created = Category.objects.get_or_create(name=category_name)
        is_available = data.get('is_available') == 'on'

        product = Product.objects.create(
            name = data['name'],
            price = data['price'],
            dis_price = data['dis_price'],
            brand = data['brand'],
            model = data['model'],
            storage = data['storage'],
            stock = data['stock'],
            is_available = is_available,
            description = data['description'],
            category = category
            )
        product.save()
        for img in files:
            image = Images.objects.create(image=img, product=product)
            image.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'add_product.html')
        
def del_category(request,id):
    categories = Category.objects.get(id=id)
    categories.delete()
    return HttpResponseRedirect('/')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_det.html', {'categories': categories})

def edit_category(request,id):
    categories = Category.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        categories.name = data['name']
        categories.image = data['image']
        categories.save()

    return render(request, 'add_category.html')

def add_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        cateory_list = Category.objects.create(
            name=name,
            image=image
        )
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