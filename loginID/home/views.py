from django.shortcuts import render, HttpResponse
from home.models import loginModel
from django.contrib import messages
from django.http import HttpResponseRedirect
# from django.contrib.auth.models import User


# Create your views here.


def index(request):
    return render(request, "index.html")


def dyn(request):

    num1=request.POST.get("num1")
    num2=request.POST.get("num2")
    params={
        "adding":int(num1)+int(num2) 
    }

    return render (request,"dyn.html",params)

def login(request):
    return render(request,"login.html")

def logout(request):
    return render(request,"logout.html")

def register(request):
    if request.method=='POST':
        # pritn("post")
        loginDet=loginModel.objects.all()
        messages.info(request, 'method is post')
        return HttpResponseRedirect('/register')

    
    return render (request,'register.html')

