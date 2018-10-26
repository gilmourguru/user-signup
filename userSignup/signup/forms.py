from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(required=False, max_length=30, help_text='Not Required, but if provided must be a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

