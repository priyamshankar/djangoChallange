from urllib import response
from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("this is a home page")
    return render(request,"index.html")
