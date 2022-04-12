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
    fetchedtext = request.GET.get("manipulativeText")
    checkStatus = request.GET.get("puncCheckbox", "off")
    puncs = """!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"""
    if checkStatus == "on":
        withoutpunc = ""
        for char in fetchedtext:
            if char not in puncs:
                withoutpunc = withoutpunc+char

        params = {
            'textBox': withoutpunc, "check": "this is a comment", }
    else:
        withoutpunc = fetchedtext

    checkCapital = request.GET.get("capitalise", "off")
    if(checkCapital == "on"):
        withoutcap = ""
        for char in fetchedtext:
            withoutcap = withoutcap+char.upper()
        params = {
            "textCapital": withoutcap
        }
    else:
        withoutcap = fetchedtext

    return render(request, "removespuncs.html", params)
