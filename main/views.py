from django.shortcuts import render

def home(request):
    return render(request,"main/home.html",{"home":"active"})

def aboutus(request):
    return render(request,"main/aboutus.html",{"aboutus":"active"})

def contactus(request):
    return render(request,"main/contactus.html", {"contactus":"active"})



