"""
URL configuration for SnapMedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from SocialMediaApp.models import *
from SocialMediaApp.views import *
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


router = routers.DefaultRouter()
router.register('Post',PostViewSet)
router.register('Like',LikeViewSet)
router.register('Comment',CommentViewSet)
router.register('SnapUser', SnapUserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createuser/',createuser),
    path('deleteuser/<int:id>/',deleteuser),
    # path('userlogin/', userlogin),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]
