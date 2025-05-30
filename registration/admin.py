from django.contrib import admin
from .models import Room, Comment, ContactMessage

# Register your models here.

# Change the Admin title and header
admin.site.site_header = "Grihalaya Sewa Admin Panel"  # Change header text
admin.site.site_title = "Grihalaya Sewa  Admin Portal"  # Change title shown on the browser tab
admin.site.index_title = "Welcome to Grihalaya Sewa  Admin Panel"  # Change the index page title

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display=['id','title','location']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['id','content']
    

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "submitted_at")
    search_fields = ("name", "email")
    list_filter = ("submitted_at",)