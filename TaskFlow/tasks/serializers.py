from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='profile.address', allow_blank=True, required=False)
    phone_no = serializers.CharField(source='profile.phone_no', allow_blank=True, required=False)
    department = serializers.CharField(source='profile.department', allow_blank=True, required=False)
    profile_pic = serializers.ImageField(source='profile.profile_pic', allow_null=True, required=False)
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','password','email','is_superuser',
                  'is_active','date_joined','address','phone_no','department','profile_pic'    
        ]

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

# class TaskSerializer(serializers.ModelSerializer):
#     due_date = serializers.DateTimeField(allow_null=True, required=False)
#     assigned_to = UserSerializer(read_only=True)

#     class Meta:
#         model = Task
#         fields = ['id', 'title', 'status', 'assigned_to', 'due_date', 'description']
    
#     def validate_due_date(self, value):
#         if value == "":
#             return None
#         return value

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_id = serializers.IntegerField(write_only=True, required=True)
    assigned_to = UserSerializer(read_only=True)


    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'due_date', 'assigned_to', 'assigned_to_id', 'project']

    
# class TaskCommentSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = TaskComment
#         fields = '__all__'
#         read_only_fields = ['user']

class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = '__all__'
        read_only_fields = ['user']  

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)