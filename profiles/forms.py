from django import forms
from django.core.exceptions import ValidationError

from .models import Student
from department.models import Department


class CompleteProfileForm(forms.Form):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"))

    # TODO Find a way to populate this using the actual list of departments available
    DEPARTMENT_CHOICES = (("CSC", "Computer Science"), ("SEN", "Software Engineering"))

    first_name = forms.CharField(disabled=True, required=False)
    last_name = forms.CharField(disabled=True, required=False)
    middle_name = forms.CharField(disabled=True, required=False)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    birthdate = forms.DateField()
    state_of_origin = forms.CharField(max_length=20)
    profile_picture = forms.ImageField()

    def clean_department(self):
        passed_department_abbr = self.cleaned_data["department"]
        department_object = Department.objects.filter(
            abbreviation=passed_department_abbr
        )
        if not department_object.exists():
            raise ValidationError("Department does not exist")
        else:
            return passed_department_abbr


class StudentCompleteProfileForm(CompleteProfileForm):
    level = forms.CharField(disabled=True, required=False)


class LecturerCompleteProfileForm(CompleteProfileForm):
    pass
