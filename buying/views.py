from django.shortcuts import render

# Create your views here.

def buying(request):
    return render(request,"buying/buying.html", {"buying":"active"})
