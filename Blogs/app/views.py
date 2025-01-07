from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from app.models import Blogs,Images
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/Userlogin')
def homepage(request):
    blog = Blogs.objects.all()
    return  render(request, 'indexpage.html',{'blog':blog})


def detail(request,id):
    blog = Blogs.objects.get(id=id)
    # like_count = blog.count_of_Like.count() 
    # comment_count = blog.count_of_comment.count()
    return render(request, 'detail.html', {'blog':blog,'user':request.user})

@login_required(login_url='/Userlogin')
def blog_histroy(request):
    try:
        profile = Profile.objects.get(user = request.user)
        if profile.is_admin:
            blog = Blogs.objects.all()  
    except Profile.DoesNotExist:
        return HttpResponseRedirect('/Userlogin')
    return render(request, 'blog_history.html', {'blog':blog})


@login_required(login_url='/Userlogin')
def userProfile(request):
    return render(request, 'profile.html',{'user':request.user})


@login_required(login_url='/Userlogin')
def create(request):
    print(request.POST)
    if request.method == 'GET':
        return render(request, 'createform.html')
    else:
        # request.method == 'POST'
        t = request.POST['title']
        d = request.POST['description']
        i = request.FILES.getlist('image')

        blogs = Blogs.objects.create(title=t, description=d, user=request.user)
        blogs.save()

        for  img in i:
            images = Images.objects.create(blog=blogs,image=img)

        return HttpResponseRedirect('/')
    

def Edit_blog(request,id):
    blogs = Blogs.objects.get(id=id)
    if request.method == 'POST':
        t = request.POST['title']
        d = request.POST['description']

        # update the information
        blogs.title = t
        blogs.description = d
        blogs.save()
        
        return HttpResponseRedirect('/')
    return render(request, 'createform.html', {'blogs':blogs})
    
    
def delete_info(request,id):
    blogs = Blogs.objects.get(id=id)
    blogs.delete() 
    return HttpResponseRedirect('/')

def DeleteImage(request,id):
    image_ids = request.POST.getlist('image')
    # print(image_ids)
    for ids in image_ids:
        img = Images.objects.get(id = ids)
        img.delete()
    return HttpResponseRedirect(f'/detail/{id}')
    
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
        else:
            return HttpResponse("user or password is not valid")
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return render(request,'loginpage.html')


def createuser(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']
        is_admin = request.POST['is_admin']
        phone_no = request.POST['phone_no']
        profile_pic = request.FILES['image']
        
        if User.objects.filter(username=username).exists():
            return HttpResponse("Error: Username already exists. Please enter another username.")

        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        user.set_password(password)
        user.save()

        profile = Profile.objects.create(is_admin=is_admin,
                                         phone_no=phone_no,
                                         user=user,
                                         profile_pic=profile_pic)
        profile.save()
        return HttpResponseRedirect("/")
    else:
        return render(request,'createuser.html')


    
    
    

    