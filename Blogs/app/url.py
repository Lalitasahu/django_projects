from .views import BlogsView  
from django.urls import path  
  
urlpattern = [  
    path('basic/', BlogsView.as_view())  
]  