from email.policy import default
from sqlite3 import paramstyle
from tkinter import OFF
from urllib import response
from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("this is a home page")
    return render(request, "index.html")


def removespuncs(request):
    fetchedtext = request.POST.get("manipulativeText")
    checkStatus = request.POST.get("puncCheckbox", "off")
    checkCapital = request.POST.get("capitalise", "off")

    puncs = """!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"""
    if checkStatus == "on":
        withoutpunc = ""
        for char in fetchedtext:
            if char not in puncs:
                withoutpunc = withoutpunc+char

        params = {
            'textBox': withoutpunc, "check": "this is a comment", }

    elif(checkCapital == "on"):
        withoutcap = ""
        for char in fetchedtext:
            withoutcap = withoutcap+char.upper()
        params = {
            "textCapital": withoutcap
        }
    else:
        withoutcap = fetchedtext
        params = {
            "textCapital": fetchedtext
        }

    return render(request, "removespuncs.html", params)
