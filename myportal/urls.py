from os import name
from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home,name ='home'),
    path('upload_file/',upload_file,name='upload_file'),
    path('search_dber/', search_dber, name='search_dber'),
    
    
    
    path('add_dber/', add_dber, name='add_dber'),
    path('send_mail/<int:pk>/', send_mail, name='send_mail'),
    path('send_mass_mails/', send_mass_mails, name='send_mass_mails'),
]
