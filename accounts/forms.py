from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, StudentProfile, TeacherProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email']
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ['user']
