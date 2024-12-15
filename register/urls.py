from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('signup/',views.signup_user,name="signup"),

    path('buy/',views.buying,name="buying"),
    path('sell/',views.selling,name="selling"),
    # path('insert_view/',views.Insert_view,name="insert_view"),
    # path('list_view/',views.List_view,name="list_view"),
    # path('detail_view/<int:id>/',views.Detail_view,name="detail_view"),
    # path('update_view/<int:id>/',views.Update_view,name="update_view"),
    # path('delete_view/<int:id>/',views.Delete_view,name="delete_view"),

 
]