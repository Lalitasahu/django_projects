from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from app.models import Blogs
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def homepage(request):
    blog = Blogs.objects.all()
    # html = ' this is my home page'
    return  render(request, 'indexpage.html',{'blog':blog})

def detail(request,id):
    blog = Blogs.objects.get(id=id)
    return render(request, 'detail.html', {'blog':blog})

def create(request):
    if request.method == 'GET':
        return render(request, 'createform.html')
    else:
        # request.method == 'POST'
        t = request.POST['title']
        d = request.POST['discription']
        u = request.POST['user']

        blogs = Blogs.objects.create(Title=t, discription=d, user=u)
        blogs.save()
        
        
        return HttpResponse('Save Successfully')

def Edit_info(request,id):
    blogs = Blogs.objects.get(id=id)
    if request.method == 'POST':
        t = request.POST['title']
        d = request.POST['discription']
        u = request.POST['user']    

        # update the information
        blogs.title = t
        blogs.discription = d
        blogs.user = u
        blogs.save()
        
        return HttpResponseRedirect('/')
    return render(request, 'createform.html', {'blogs':blogs})
    
    
def delete_info(request,id):
    blogs = Blogs.objects.get(id=id)
    blogs.delete()
    
    return HttpResponseRedirect('/')


def Userlogout(request):
    logout(request)
    return HttpResponseRedirect("/")


def Userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/")
            # return HttpResponse("user and password is correct")
        else:
            return HttpResponse("user or password is not valid")

    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return render(request,'loginpage.html')


def createUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            # password=password,
            email=email
        )

        user.set_password(password)

        user.save()
        return HttpResponseRedirect("/")


    else:
        return render(request,'createuser.html')


    
    
    

    