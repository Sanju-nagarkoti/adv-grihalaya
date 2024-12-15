from django import forms
from django.core.validators import RegexValidator
from .models import Room

class RoomForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Room
        fields='__all__'

        widgets = {
                    'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter room title'}),
                    'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
                    'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
                    'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
                    'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter room description'}),
                }