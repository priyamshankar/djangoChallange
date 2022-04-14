from django.shortcuts import render, HttpResponse

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
    return render (request,'request.html')

