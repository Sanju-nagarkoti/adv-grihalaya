from django.urls import path
from . import views

urlpatterns = [
    path('buying/',views.buying,name="buying"),
]
