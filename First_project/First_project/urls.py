"""
URL configuration for First_project project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app.views import *
from rest_framework import routers



router = routers.DefaultRouter()
router.register('User',UserSet)
router.register('Profile',ProfileSet)
router.register('Product',ProductSet)
router.register('Order',OrderSet)
router.register('Cart',CartSet)
router.register('Category',CategorySet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    path("createuser/",createuser),
    path('userlogin/',userlogin),
    path('userlogout/',userlogout),
    path('userprofile/',userprofile),
    path('add_category/',add_category),
    path('edit_category/<int:id>/',edit_category),
    path('category_list/',category_list),
    path('del_category/<int:id>/',del_category),
    path('del_product/<int:id>/',del_product),
    path('edit_product/<int:id>/',edit_product),
    path('pro_list/<int:id>/',pro_list),
    path('DeleteImage/<int:id>/',DeleteImage),
    path('add_product/<int:id>/',add_pro_list),
    path('pro_detail/<int:id>/',pro_detail),
    path('order_item/<int:id>/',order_item),
    path('order_history/',order_history),
    path('order_detail/<int:id>/',order_detail),
    path('cancel_order/<int:id>/',cancel_order),
    path('confirm_order/<int:id>/',confirm_order),
    path('add_to_cart/<int:id>/',add_to_cart),
    path('show_cart/',show_cart),
    path('remove_cart/<int:id>/',remove_cart),
    path('search/',searching),
    path('add_review/<int:id>/',add_review),
    path('edit_review/<int:id>/',edit_review),
    path('delete_review/<int:id>/',delete_review),
    path('show_reviews/',show_reviews),
    path('ajax/',ajax_page),
    path('api/', include(router.urls)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


