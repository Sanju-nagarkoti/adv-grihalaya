from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def login_user(request):
    if request.method == "POST":
        login_username = request.POST['username']
        login_password = request.POST['password']

        #Check for empty fields
        if not login_username or not login_password:
            messages.error(request, 'All fields are required')
            return redirect('/register/login/')

        #Login
        user = authenticate(request, username = login_username, password = login_password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('/register/login/')
    else:
        return render(request,"register/login.html")
    
def logout_user(request):
    logout(request)
    return redirect('/register/login/')
    
def signup_user(request):
    if request.method == "POST":

        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        address = request.POST['address']
        phoneno = request.POST['phoneno']
        

        #Check for empty fields
        if not fname or not lname or not username or not email or not password or not repassword:
            messages.error(request, 'All fields are required')
            return redirect('/register/signup/')

        # Check if passwords match
        if password != repassword:
            messages.error(request, 'Passwords do not match')
            return redirect('/register/signup/')

        # Validate password
        try:
            validate_password(password)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect('/register/signup/')

        # Check if username already exists
        if User.objects.filter(username__iexact=username).exists():
            messages.error(request, "Username is already taken")
            return redirect('/register/signup/')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
            return redirect('/register/signup/')

        # Create the user
        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, 'Account created successfully. You can now login.')
        return redirect('/register/login/')
    else:
        return render(request, "register/signup.html")

@login_required(login_url='login')
def buying(request):
    return render(request,"register/buying.html", {"buying":"active"})

@login_required(login_url='login')
def selling(request):
    return render(request,"register/selling.html", {"selling":"active"})










