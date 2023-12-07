from django import forms

from .models import Department
from profiles.models import Lecturer


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            'name',
            'head_of_department',
            'description',
            'location',
            'logo',
            'abbreviation'
        ]