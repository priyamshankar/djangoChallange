from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
# from django.views.generic.edit  import CreateView

# Create your views here.


def index(request):
    # return HttpResponse("this is a homepage")
    return render(request,"index.html")

# def about2(request):


def about(request):
    # return HttpResponse("this is a priyam page")
    return render(request,"about.html")

def contact(request):
    # return HttpResponse("this is a contact us page")
    return render(request,"contact.html")
