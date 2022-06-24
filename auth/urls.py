from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    
    
    # path('docpat', views.docpat, name = "docpat"),



    path('', views.home, name = "home"),
    path('signUpform', views.signup, name="signUpform"),
    path('signInform', views.signin, name="signInform"),
    path('signOutform', views.signout, name="signOutform"),
]
