from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,"main/home.html",{"home":"active"})

def aboutus(request):
    return render(request,"main/aboutus.html",{"aboutus":"active"})

def contactus(request):
    return render(request,"main/contactus.html", {"contactus":"active"})




