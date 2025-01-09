"""
URL configuration for Blogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path, include  
from django.conf import settings
from django.contrib import admin
from django.urls import path
from app.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('blog',BlogSet)
router.register('user',UserSet)
router.register('likes',LikesSet)

# router=routers.DefaultRouter()
# router.register('blog',BlogSet)
# router.register('user',UserSet)
# router.register('user',UserSet),
# router.register('photo',PhotoSet),



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    path('detail/<int:id>',detail),
    path('create/',create),
    path('Edit_blog/<int:id>',Edit_blog),
    path('delete_info/<int:id>',delete_info),
    path('Userlogout/',Userlogout),
    path('Userlogin/',Userlogin),
    path('createuser/',createuser),
    path('userProfile/',userProfile),
    path('blog_histroy/',blog_histroy),
    path('DeleteImage/<int:id>',DeleteImage),
    # path('api/', include('app.url'))
    path('api/',include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
