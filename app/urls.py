
from django.urls import path,include
from .views import(
    index,
	encode,
	decode)

urlpatterns = [
	# url(r'^$', views.index, name='index'),
	# url(r'^encode$', views.encode, name='encode'),
	# url(r'^decode$', views.decode, name='decode')
	path('',index,name='index'),
	path('encode',encode,name='encode'),
	path('decode',decode,name='decode'),

]
