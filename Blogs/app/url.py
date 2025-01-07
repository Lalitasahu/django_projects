from .views import BlogsView  
from django.urls import path
  
urlpatterns = [  
    path('blogs/', BlogsView.as_view())  
]  