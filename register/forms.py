from django import forms
from django.core.validators import RegexValidator
from .models import Room

class RoomForm(forms.ModelForm):
    # Adding custom validation for phone number using RegexValidator
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Enter a valid phone number (e.g., +999999999)."
    )

    class Meta:
        model = Room
        fields = '__all__'
        exclude=['user']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter room title'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter room description'}),
            'seller_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter seller name'}),
            'seller_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter seller address'}),
            'seller_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter seller email'}),
            'seller_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter seller phone number'}),
            'status': forms.Select(choices=[('available', 'Available'), ('sold', 'Sold')], attrs={'class': 'form-control'}),
        }

    # Custom validation for the phone number field
    seller_phone = forms.CharField(
        validators=[phone_validator],
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter seller phone number'})
    )