from django.contrib import admin
from .models import Room

# Register your models here.

# Change the Admin title and header
admin.site.site_header = "Grihalaya Sewa Admin Panel"  # Change header text
admin.site.site_title = "Grihalaya Sewa  Admin Portal"  # Change title shown on the browser tab
admin.site.index_title = "Welcome to Grihalaya Sewa  Admin Panel"  # Change the index page title

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display=['id','title','location']
    
    
 


