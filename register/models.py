from django.db import models

class Room(models.Model):
    title = models.CharField(max_length=200)  # Title of the room listing
    location = models.CharField(max_length=255)  # Location of the room
    price =models.CharField(max_length=255)  # Price for renting the room
    image = models.ImageField(upload_to='room_images/')  # Image of the room
    description = models.TextField()  # Description of the room

    def __str__(self):
        return self.title #to represent table 