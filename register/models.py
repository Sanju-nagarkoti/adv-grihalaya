# models.py
from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.TextField()
    seller_name = models.CharField(max_length=255)
    seller_address = models.TextField()
    seller_email = models.EmailField()
    seller_phone = models.CharField(max_length=15)
    status = models.CharField(
        max_length=50,
        choices=[('available', 'Available'), ('sold', 'Sold')],
        default='available'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms', null=True, blank=True)

    def __str__(self):
        return self.title


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return f"Image for {self.room.title}"
    
    
class Comment(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='comments')  # Link to the Room
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Optional link to the User
    content = models.TextField()  # Comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the comment was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp of when the comment was last updated

    def __str__(self):
        return f"Comment by {self.user.username if self.user else 'Anonymous'} on {self.room.title}"
    
