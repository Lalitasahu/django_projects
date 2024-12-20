"""
URL configuration for HotelBooking project.

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
from django.urls import path
from app.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    path('Add_rooms/',Add_rooms),
    path('detail/<int:id>/',detail),
    path('delete_rooms/<int:id>/',delete_rooms),
    path('Booking_edi/<int:id>/',Booking_edi),
    path('Confirm_booking/<int:id>/',Confirm_booking),
    path('booking_history/',booking_history),
    path('userlogout/',userlogout),
    path('userlogin/',userlogin),
    path('createuser/',createuser),
    path('detail_confirm_booking/<int:id>/',detail_confirm_booking),
    path('Edit_confirm_booking/<int:id>/',Edit_confirm_booking),
    path('Delete_confirm_booking/<int:id>/',Delete_confirm_booking),
    path('check_out/<int:id>/',check_out),
    path('check_out_view/<int:id>/',check_out_view),
    path('cancel/<int:id>',cancel_booking),
    path('profile/',get_profile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
