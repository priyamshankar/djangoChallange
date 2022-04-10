from django.shortcuts import render, HttpResponse
# from matplotlib.style import context

# Create your views here.


def index(request):
    context ={
        "vary" : "home variable"
    }
    return render(request, "index.html",context)
    # return HttpResponse("this is a home page")

# def about2(request):


def about(request):
    # return HttpResponse("this is a priyam page")
    return render(request, "about.html")


def contact(request):
    # return HttpResponse("this is a contact us page")
    context={
        "variable":"this is the contact variable made dynamically"
    }
    return render(request, "contact.html",context)
