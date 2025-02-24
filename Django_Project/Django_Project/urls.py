"""
URL configuration for Django_Project project.

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
from django.contrib import admin
from django.urls import path, include
from app.views import * 
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


router = routers.DefaultRouter()
router.register('product',ProductSet)
router.register('Images',ImagesSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    path('Createpage/',Createpage),
    path('createuser/',createuser),
    path('loginuser/',loginuser),
    path('logoutuser/',logoutuser),
    # path('category_items/<str:category_name>/',category_items),
    path('edit_product/<int:id>',edit_product),
    path('delete_product/<int:id>',delete_product),
    path('detailpage/<int:id>',detailpage),
    path('categories/',categories),
    path('laptop/',laptop),
    path('Stationery/',Stationery),
    path('toys/',toys),
    path('api/',include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
