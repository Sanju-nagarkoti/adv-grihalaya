from django.shortcuts import render

# Create your views here.
def selling(request):
    return render(request,"selling/selling.html", {"selling":"active"})
