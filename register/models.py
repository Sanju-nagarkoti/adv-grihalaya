from django.db import models
from django.contrib.auth.models import User  # Import the User model


class Room(models.Model):
    title = models.CharField(max_length=200)  # Title of the room listing
    location = models.CharField(max_length=255)  # Location of the room
    price = models.CharField(max_length=255)  # Price for renting the room
    image = models.ImageField(upload_to='room_images/')  # Image of the room
    description = models.TextField()  # Description of the room

    # Seller's information
    seller_name = models.CharField(max_length=255)  # Seller's name
    seller_address = models.TextField()  # Seller's address
    seller_email = models.EmailField()  # Seller's email
    seller_phone = models.CharField(max_length=15)  # Seller's phone number
    status = models.CharField(
        max_length=50,
        choices=[('available', 'Available'), ('sold', 'Sold')],
        default='available'
    )  # Room status

    # Link to the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms', null=True, blank=True)  

    def __str__(self):
        return self.title  # To represent table with the room title
    
