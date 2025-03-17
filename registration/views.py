from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RoomForm, CommentForm, RoomImageForm, ContactMessageForm
from .models import Room, Comment, RoomImage
from django.http import HttpResponseForbidden
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db import transaction
from django.contrib.auth.forms import PasswordChangeForm



# Create your views here.

def profile(request):
    return render(request,"registration/profile.html",{"profile":"active"})

def login_user(request):
    if request.method == "POST":
        login_username = request.POST['username']
        login_password = request.POST['password']

        #Check for empty fields
        if not login_username or not login_password:
            messages.error(request, 'All fields are required')
            return redirect('registration:login')

        #Login
        user = authenticate(request, username = login_username, password = login_password)
        if user is not None:
            login(request, user)
            return redirect('/profile/')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('registration:login')
    else:
        return render(request,"registration/login.html")
    
def logout_user(request):
    logout(request)
    return redirect('registration:login')
    
def signup_user(request):
    if request.method == "POST":

        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        

        #Check for empty fields
        if not fname or not lname or not username or not email or not password or not repassword:
            messages.error(request, 'All fields are required')
            return redirect('/accounts/signup/')

        # Check if passwords match
        if password != repassword:
            messages.error(request, 'Passwords do not match')
            return redirect('/accounts/signup/')

        # Validate password
        try:
            validate_password(password)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect('/accounts/signup/')

        # Check if username already exists
        if User.objects.filter(username__iexact=username).exists():
            messages.error(request, "Username is already taken")
            return redirect('/accounts/signup/')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
            return redirect('/accounts/signup/')

        # Create the user
        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, 'Account created successfully. You can now login.')
        return redirect('/accounts/login/')
    else:
        return render(request, "registration/signup.html")

# Selling
# views.py
@login_required(login_url='registration:login')
def selling(request, pk):
    rooms = Room.objects.filter(user_id=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST)
        images = request.FILES.getlist('image')  # Retrieve multiple files
        if form.is_valid():
            room = form.save(commit=False)
            room.user = request.user
            room.save()

            # Save each uploaded image
            for image in images:
                RoomImage.objects.create(room=room, image=image)

            return redirect('registration:buying')
    else:
        form = RoomForm()
    return render(request, "registration/selling/sell_room_insert.html", {
        "selling": "active",
        'form': form,
        'rooms': rooms
    })

# Room Details View
@login_required(login_url='registration:login')
def Sell_Room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    images = room.images.all()  # Retrieve all images related to the room
    return render(request, 'registration/selling/sell_room_detail.html', {
        'room': room,
        'images': images
    })

# Room Update View
@login_required(login_url='registration:login')
def Sell_Room_update(request, pk):
    room = get_object_or_404(Room, pk=pk)

    if room.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this room.")

    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        images = request.FILES.getlist('images')  # Get all uploaded images

        if form.is_valid():
            with transaction.atomic():  # Ensure atomic save for room and images
                updated_room = form.save()

                # Add new images to the room
                for image in images:
                    RoomImage.objects.create(room=updated_room, image=image)

            return redirect('registration:sell_room_detail', pk=room.pk)
    else:
        form = RoomForm(instance=room)

    return render(request, 'registration/selling/sell_room_update.html', {
        'form': form,
        'room': room,
    })

# Room Delete View
def Sell_Room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('registration:buying')
    return render(request, 'registration/selling/sell_room_delete.html', {'room': room})

# Buying
@login_required(login_url='registration:login')  # to visit buying page, first login
def buying(request):  # list room
    rooms = Room.objects.prefetch_related('images').all()  # Efficiently fetch rooms with related images
    return render(request, "registration/buying/buy_room_list.html", {"buying": "active", 'rooms': rooms})

# Room Details View
def Buy_Room_detail(request, pk):
    # Fetch the room with its related images
    room = get_object_or_404(Room.objects.prefetch_related('images'), pk=pk)
    comments = room.comments.all()  # Fetch related comments

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Email logic
            subject = "Message from Grihalaya"
            message = request.POST['content']
            from_email = "sanjunagarkoti44@gmail.com"  # Your sender email
            recipient_list = [room.seller_email]  # Seller's email from the Room object
            user_email = request.user.email if request.user.is_authenticated else "Anonymous"

            # Render message template
            email_message = render_to_string('registration/message.html', {
                'name': room.seller_name,
                'message': message,
                'user_email': user_email,  # Include user email in the context
            })

            # Send the email
            send_mail(subject, email_message, from_email, recipient_list, fail_silently=False)

            # Save the comment
            comment = form.save(commit=False)
            comment.room = room  # Associate the comment with the room
            comment.user = request.user if request.user.is_authenticated else None
            comment.save()

            # Redirect after processing
            return redirect('registration:buy_room_detail', pk=room.pk)
    else:
        form = CommentForm()

    return render(request, 'registration/buying/buy_room_detail.html', {
        'room': room,
        "buying": "active",
        'comments': comments,
        'form': form
    })

@login_required(login_url='registration:login')
def delete_room_image(request, image_pk):
    image = get_object_or_404(RoomImage, pk=image_pk)

    if image.room.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this image.")

    image.delete()
    return redirect('registration:sell_room_update', pk=image.room.pk)


# about me
@login_required
def about_me(request):
    # Initialize password form
    password_form = PasswordChangeForm(user=request.user)
    
    if request.method == "POST":
        # Check which form was submitted
        if "update_info" in request.POST:  # Handle user info update
            first_name = request.POST.get("first_name", "")
            last_name = request.POST.get("last_name", "")
            email = request.POST.get("email", "")

            # Update user fields without affecting the password
            user = request.user
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            messages.success(request, "Your information has been updated successfully.")
            return redirect("registration:about_me")

        elif "change_password" in request.POST:  # Handle password change
            password_form = PasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                password_form.save()
                messages.success(request, "Your password has been updated successfully.")
                return redirect("registration:about_me")  # Prevent resubmission
            else:
                messages.error(request, "Please correct the errors below.")
    
    return render(request, "registration/aboutme.html", {
        "password_form": password_form,
    })


@login_required
def change_password(request):
    password_form = PasswordChangeForm(user=request.user)
    
    if request.method == "POST":
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            password_form.save()
            messages.success(request, "Your password has been updated successfully.")
            return redirect("registration:change_password")  # Prevent resubmission
        else:
            messages.error(request, "Please correct the errors below.")

    return render(request, "registration/change_password.html", {
        "password_form": password_form,
    })


def contactus(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("registration:contactus")  # Redirect to avoid form resubmission
        else:
            messages.error(request, "There was an error. Please correct the form.")
    else:
        form = ContactMessageForm()

    return render(request, "registration/contactus.html", {"form": form, "messages": messages.get_messages(request), "contactus": "active"})




