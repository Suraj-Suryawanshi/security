from unicodedata import name
from django.contrib import admin
from django.urls import path
from userReg import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path ('logout',views.logout,name='logout'),

]
