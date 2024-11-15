from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),
        }

    # Custom validation error messages
    error_messages = {
        'name': {
            'required': 'Please provide your name.',
        },
        'email': {
            'required': 'Please provide an email address.',
            'invalid': 'Please enter a valid email address.',
        },
        'phone': {
            'required': 'Please provide a phone number.',
        },
        'message': {
            'required': 'Please provide a message.',
        },
    }
