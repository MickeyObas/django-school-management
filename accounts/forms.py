from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['account_type', 'first_name', 'last_name', 'middle_name', 'email', 'password1', 'password2']