from django.urls import path
from . import views

urlpatterns = [
    path('selling/',views.selling,name="selling"),
]
