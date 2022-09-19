from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, StudentProfile, TeacherProfile, Student, Teacher

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email']
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email']

class StudentUserCreationForm:
    class Meta:
        model = Student
        fields = ['email']

class StudentUserCreationForm:
    class Meta:
        model = Teacher
        fields = ['email']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ['user']

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        exclude = ['user']
    
