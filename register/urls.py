from django.urls import path
from . import views

app_name='register'

urlpatterns = [
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('signup/',views.signup_user,name="signup"),

    path('buy/',views.buying,name="buying"),#room_list
    path('sell/<int:pk>/',views.selling,name="selling1"),#room_insert
    path('sell/',views.selling,name="selling2"),
    path('room_detail/<int:pk>/',views.Room_detail,name="room_detail"),
    path('room_update/<int:pk>/',views.Room_update,name="room_update"),
    path('room_delete/<int:pk>/',views.Room_delete,name="room_delete"),
    

 
]