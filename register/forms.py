# forms.py
from django import forms
from django.core.validators import RegexValidator
from .models import Room, RoomImage, Comment
from .widgets import MultiFileInput

class RoomForm(forms.ModelForm):
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Enter a valid phone number (e.g., +999999999)."
    )

    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter room title'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter room description'}),
            'seller_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter seller name'}),
            'seller_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter seller address'}),
            'seller_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter seller email'}),
            'seller_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter seller phone number'}),
            'status': forms.Select(choices=[('available', 'Available'), ('sold', 'Sold')], attrs={'class': 'form-control'}),
        }

    seller_phone = forms.CharField(
        validators=[phone_validator],
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter seller phone number'})
    )


class RoomImageForm(forms.ModelForm):
    class Meta:
        model = RoomImage
        fields = ['image']
        widgets = {
            'image': MultiFileInput(attrs={'class': 'form-control', 'multiple': True}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Fields to be included in the form
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your comment here...',
                'rows': 2,  # Two lines height
                'cols': 40  # Small width
            }),
        }
        labels = {
            'content': 'Your Comment',
        }