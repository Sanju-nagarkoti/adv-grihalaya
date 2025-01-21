from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name='registration'

urlpatterns = [
    path('',views.profile,name="profile"),
    path('profile/',views.profile),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('signup/',views.signup_user,name="signup"),

    path('sell/<int:pk>/',views.selling,name="selling"),#room_insert, room_list==id
    path('sell/',views.selling,name="selling2"),
    path('sell_room_detail/<int:pk>/',views.Sell_Room_detail,name="sell_room_detail"),
    path('sell_room_update/<int:pk>/',views.Sell_Room_update,name="sell_room_update"),
    path('sell_room_delete/<int:pk>/',views.Sell_Room_delete,name="sell_room_delete"),

    path('buy/',views.buying,name="buying"),#room_list
    path('buy_room_detail/<int:pk>/',views.Buy_Room_detail,name="buy_room_detail"),
    
    path('delete-room-image/<int:image_pk>/', views.delete_room_image, name='delete_room_image'),
    
    
 
]