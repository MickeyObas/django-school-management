from django import forms
from django.core.exceptions import ValidationError

from .models import Student
from department.models import Department
from department.choices import DEPARTMENT_CHOICES


class CompleteProfileForm(forms.Form):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"))

    first_name = forms.CharField(
        disabled=True,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name = forms.CharField(
        disabled=True,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    middle_name = forms.CharField(
        disabled=True,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.Select(attrs={"class": "form-select"})
    )
    department = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES, widget=forms.Select(attrs={"class": "form-select"})
    )
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"})
    )
    state_of_origin = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    profile_picture = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "form-control", "type": "file"})
    )

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
    level = forms.CharField(
        disabled=True,
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )


class LecturerCompleteProfileForm(CompleteProfileForm):
    pass


class ApproveCoursesAdminForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["matric_number", "department", "level", "courses_approved"]
        widgets = {
            "matric_number": forms.TextInput(attrs={"readonly": True}),
            "department": forms.Select(attrs={"disabled": True}),
            "level": forms.Select(attrs={"disabled": True}),
        }
