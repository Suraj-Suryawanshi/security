from django.shortcuts import render
from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from io import BytesIO
import os

from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.


def news(request):

    newsapi = NewsApiClient(api_key='f54a699ca5484f138e397c566fa40705')
    top = newsapi.get_top_headlines(sources='techcrunch')

    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
    # 
    return render(request,'news.html', context={"mylist": mylist})

def about(request):
    return render(request,'about.html')

def index(request):
    return render(request, "index.html")


def services(request):
    return render(request, 'services.html')


def crypto(request):
    return render(request, 'crypto/home.html')
