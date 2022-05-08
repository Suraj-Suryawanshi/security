from django.contrib import admin
from django.urls import path

from home import views


urlpatterns = [
    path('',views.index, name='index'),
    path('services/',views.services, name='services'),
    path('news/',views.news, name='news'),
    path('about/',views.about, name='about'),
    
    # path('crypto',views.crypto,name='crypto')
]
