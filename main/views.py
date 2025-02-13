from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def profile(request):
    return render(request,"registration/profile.html",{"profile":"active"})

def aboutus(request):
    return render(request,"main/aboutus.html",{"aboutus":"active"})






