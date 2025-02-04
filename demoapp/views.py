from django.shortcuts import render ,redirect
from django.http import  HttpResponse
from .models import services
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def index(request):
    service = services.objects.all()
    return render(request,'index.html',{"services":service})

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request,'Email already existis')
                return redirect ('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request,'Username Already Exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password does not match')
            return redirect('register')
    else:
        return render(request,'register.html')

def nextpage(request):
    # words = request.POST['Value']
    # num_of_words=len(words.split())
    return render (request,'portfolio-details.html')