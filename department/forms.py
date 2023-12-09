from django import forms

from .models import Department
from profiles.models import Student, Lecturer


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            "name",
            "head_of_department",
            "description",
            "location",
            "logo",
            "abbreviation",
        ]


class ApproveStudentsCoursesForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["matric_number", "department", "level", "courses_approved"]
        widgets = {
            "matric_number": forms.TextInput(attrs={"readonly": True}),
        }
