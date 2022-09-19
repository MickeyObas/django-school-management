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

class TeacherUserCreationForm:
    class Meta:
        model = Teacher
        fields = ['email']

class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile
        fields = ['first_name', 'last_name', 'birth_date', 'school_grade']
        widgets = {'birth_date': forms.SelectDateWidget(years=range(1980, 2011))}
        labels = {'first_name':'First Name', 'last_name': 'Last Name', 'birth_date': 'Birthday', 'school_grade': 'Class'}

class TeacherProfileForm(forms.ModelForm):
    
    class Meta:
        model = TeacherProfile
        fields = ['first_name', 'last_name', 'birth_date', 'school_grade']
        widgets = {'birth_date': forms.SelectDateWidget(years=range(1960, 2000))}
        labels = {'first_name':'First Name', 'last_name': 'Last Name', 'birth_date': 'Birthday', 'school_grade': 'Class'}
    
