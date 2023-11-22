from django import forms 

from .models import CourseDocument


class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = CourseDocument
        fields = ['title', 'course', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'})
        }