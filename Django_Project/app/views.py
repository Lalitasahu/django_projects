
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from app.models import Product


def homepage(request):
    prd = Product.objects.filter(is_deleted=False)
    return render(request, 'Indexpage.html', {'prd': prd})


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


def Createpage(request):
    if request.method == "POST":
        T = request.POST['title']
        P = request.POST['price']
        D = request.POST['description']

        prod = Product.objects.create(title=T, price=P, description=D)
        prod.save()
        return HttpResponseRedirect('/')
    return render(request, 'Listpage.html')



# def Createpage(request):
#     if request.method == "POST":
#         T = request.POST['title']
#         P = request.POST['price']
#         D = request.POST['description']
#         C = request.POST['category']

#         prod = Product.objects.create(title=T, price=P, description=D, category=C)
#         prod.save()
#         return HttpResponseRedirect('/')
#     return render(request, 'Listpage.html')

# def category_items(request, category_name):
#     prd = Product.objects.filter(category=category_name, is_deleted=False)
#     return render(request, 'categorie.html', {'prd': prd, 'category_name': category_name})


def detailpage(request,id):
    Products = Product.objects.get(id=id)
    return render(request,'detail.html',{'Products':Products})
    

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
