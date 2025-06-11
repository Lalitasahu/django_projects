from django.shortcuts import render, HttpResponse,  HttpResponseRedirect
from django.contrib.auth import authenticate, login
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from SocialMediaApp.models import *
from .serializers import  *
# from .models import SnapUser 
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Ensure only authenticated users can create posts
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            raise PermissionDenied("You must be logged in to create a post.")


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]


class SnapUserViewSet(viewsets.ModelViewSet):
    queryset = SnapUser.objects.all()
    serializer_class = SnapUserSerializer


# def userlogin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request,user)
#             return HttpResponseRedirect("/")
#         else:
#             return HttpResponse('user and password not valid')
#     else:
#         if request.user.is_authenticated:
#             return HttpResponseRedirect("/")
#         return render(request,'login.html')
    

def deleteuser(request,id):
    user = User.objects.get(id = id)
    user.delete()
    return HttpResponseRedirect('/')

def createuser(request):
    if request.method == "POST":
        data = request.POST
        files = request.FILES

        if User.objects.filter(first_name=data['first_name']).exists():
            return HttpResponse("Error: Username already exists. Please enter another username.")
        
        user = User.objects.create(
            username = data['username'],  # Assuming first_name is used as username
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email']
        )

        user.set_password(data['set_password'])
        user.save()


        snapuser = SnapUser.objects.create(
            user = user,
            profile_picture = files['profile_picture'],
            bio = data['bio'] ,
            phone_no = data['phone_no'],
            address = data['address'],
        )
        snapuser.save()
    return render(request, 'createnewuser.html')
