
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from app.models import Product, Images, User, User_profile
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .serializers import ProductSerializer, ImagesSerializer
from rest_framework import viewsets
from django.contrib.auth import authenticate, login, logout


class ProductSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ImagesSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/')

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("user or password is not valid")
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
    return render(request, 'login.html')
        

def createuser(request):
    # print(request.POST)
    if request.method == "GET":
        return render(request, 'createuser.html')
    else:
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        profile_pic = request.FILES['profile_pic']

    user = User.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
    )
    user.set_password(password)
    user.save()

    user_profile = User_profile.objects.create(
        phone_no=phone_no,
        profile_pic=profile_pic,
        user=user
    )
    user_profile.save()
    return HttpResponseRedirect('/')

def homepage(request):
    prd = Product.objects.filter(is_deleted=False)
    return render(request, 'Indexpage.html', {'prd': prd})

def detailpage(request,id):
    Products = Product.objects.get(id=id)
    return render(request,'detail.html',{'Products':Products})

def Createpage(request):
    print(request.POST)
    if request.method == "POST":
        T = request.POST['title']
        P = request.POST['price']
        D = request.POST['description']
        I = request.FILES.getlist('image')

        # Save Product instance
        prd = Product.objects.create(title=T, price=P, description=D, user=request.user)
        # breakpoint()
        # Save associated images
        for img in I:
            image = Images.objects.create(product=prd, image=img)
            image.save()
        return HttpResponseRedirect('/')
    return render(request, 'Listpage.html')


def edit_product(request, id):
    Product_upadated = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        T = request.POST.get('title')
        P = request.POST.get('price')
        D = request.POST.get('description')

        Product_upadated = Product.objects.get(id=id)

        Product_upadated.title = T
        Product_upadated.price = P
        Product_upadated.description = D
        Product_upadated.save()      
        return HttpResponseRedirect('/')

    return render(request, 'Listpage.html', {'Product_upadated': Product_upadated})


def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.is_deleted = True
    # product.product.objects.delete()
    product.save()

    return HttpResponseRedirect('/')

def categories(request):
    Products_ = Product.objects.all()
    return render(request, 'categorie.html', {'Products_':Products_})

def laptop(request):
    prd = Product.objects.filter(is_deleted=False)
    return render(request, 'laptop.html', {'prd': prd})

def Stationery(request):
    prd = Product.objects.filter(is_deleted=False)
    return render(request, 'Stationery.html', {'prd': prd})

def toys(request):
    prd = Product.objects.filter(is_deleted=False)
    return render(request, 'toys.html', {'prd':prd})
