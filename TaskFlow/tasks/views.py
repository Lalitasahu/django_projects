# Create your views here.
from django.shortcuts import render, HttpResponse

from rest_framework import viewsets,permissions, status
from rest_framework.response import Response
from .models import *
from .serializers import *
import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken



class LoginAPI(APIView):    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def current_user(request):
    user = request.user
    profile = request.user.profile
    return Response({
        "user_id":user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "password": user.password,
        "email": user.email,
        "is_superuser": user.is_superuser,

        "address": profile.address,
        "phone_no": profile.phone_no,
        "profile_pic": profile.profile_pic.url if profile.profile_pic else None,  
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        username = request.data.get("username")
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        address = request.data.get('address')
        password = request.data.get('password')
        phone_no = request.data.get('phone_no')
        profile_pic = request.FILES.get('profile_pic')  

        # Create User
        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_superuser=False,
            is_active=True,
            date_joined=datetime.datetime.now()
        )
        user.set_password(password)
        user.save()

        # Create Profile
        profile = Profile.objects.create(
            user=user,
            address=address,
            phone_no=phone_no,
            profile_pic=profile_pic
        )
        profile.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    

# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

#     def create(self, request, *args, **kwargs):
#         title = request.data.get("title")
#         description = request.data.get('description')
#         status = request.data.get('status', 'TODO')
#         assigned_to_id = request.data.get('assigned_to')
#         due_date = request.data.get('due_date')
#         completed = request.data.get('completed', False)

#         assigned_to = User.objects.get(id=assigned_to_id)
#         tasks = Task.objects.create(
#             title = title,
#             description = description,
#             status = status,
#             assigned_to = assigned_to,
#             due_date = due_date,
#             completed = completed
#         )
#         tasks.save()
#         serializer = TaskSerializer(Task)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class ProjectViewSet(viewsets.ModelViewSet):    
    # permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskCommentViewSet(viewsets.ModelViewSet):
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
