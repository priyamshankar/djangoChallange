from django.http import HttpRequest
from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("this is a homepage")

def about(request):
    return HttpRequest("this is a priyam page")