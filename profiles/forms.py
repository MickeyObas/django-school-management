from django import forms

from .models import Student

class StudentProfileForm(forms.Form):
    pass

class StudentProfileFormm(forms.ModelForm):

    first_name = forms.CharField(max_length=100, label='First Name', widget={
            forms.TextInput(attrs={'disabled': True})
        })
    last_name = forms.CharField(max_length=100, label='Last Name', widget={
        forms.TextInput(attrs={'disabled': True})
    })
    middle_name = forms.CharField(max_length=100, label='Middle Name', widget={
        forms.TextInput(attrs={'disabled': True})
    })
    
    class Meta:

        model = Student

        fields = ['profile_picture', 'birthdate', 'department', 'gender', 'state_of_origin']

        widgets = {
            'birthdate': forms.DateInput(attrs={
                'disabled': True
            }),
            'department': forms.Select(attrs={
                'disabled': True
            }),
            'gender': forms.Select(attrs={
                'disabled': True
            }),
            'state_of_origin': forms.TextInput(attrs={
                'disabled': True
            }),
        }