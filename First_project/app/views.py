
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

@login_required(login_url='/userlogin')
def cancel_order(request,id):
    # product = Product.objects.get(id=id)
    order = get_object_or_404(Order, id=id)
    order.status = "cancelled"
    # order.product.is_available = True
    # order.product.save()
    order.save()
    return HttpResponseRedirect('/')

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
        if quantity > product.stock:
            return render(request, 'order_pro.html', {'product': product,
                                                      'error': 'Quantity exceeds available stock.'})
        order = Order.objects.create(
            user=request.user,
            product=product.name,
            price=product.price,
            quantity=quantity,
            shipping_address=data['shipping_address'],
            status=data['status']
        )
        order.save()
  
        # Update product stock
        product.stock -= quantity
        product.is_available = product.stock > 0  
        product.save()

        # Redirect to the product detail page
        return HttpResponseRedirect('/')

    return render(request, 'order_pro.html', {'product': product})


def pro_detail(request,id):
    product = Product.objects.get(id=id)
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
    product = Product.objects.filter(category_id=id)
    return render(request, 'product_list.html', {'product':product,'category_id':id})

@login_required(login_url='/userlogin')
def add_pro_list(request,id):
    if request.method == 'POST':
        data = request.POST
        files = request.FILES.getlist('image')
        product = Product.objects.create(
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