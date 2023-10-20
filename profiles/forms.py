from django import forms

from .models import Student

class StudentProfileForm(forms.Form):
    pass

class StudentProfileFormm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'