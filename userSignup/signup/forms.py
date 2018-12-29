from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.conf import settings
from django.contrib.auth import authenticate, login


class SignUpForm(UserCreationForm):
    
    email = forms.CharField(required=False, max_length=20, help_text='Not Required, but if provided must be a valid email address.')
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

# class LoginForm (login):
#     class Meta:
#         model = 