from django.contrib import messages
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth



# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user =auth.authenticate(username=username,password=password )

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials")
            print('Invalid')
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        pass2 = request.POST['pass2']

        if password == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist.')
                print('Invalid username')
                return redirect('register')
                
            if User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                print("invalid email")
                return redirect('register')     
                
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                print('User Created')
                return redirect('login')
                
        else:
            messages.info(request,"password does not matched")
            return redirect('register')
        # return redirect('/')

    else:
        return render(request,'register.html')

