from typing import Any
from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
from django.http.request import HttpRequest
from django.urls import reverse
from django import forms

from .models import User
from core.admin import custom_admin_site
from profiles.models import Student, Lecturer


class StudentInline(admin.StackedInline):

    model = Student
    can_delete = False
    verbose_name = "Student Profile"
    readonly_fields = ['matric_number', 'birthdate', 'gender', 'level', 'full_name', 'age', 'state_of_origin']
    fieldsets = [
        (None, {
            'fields': ['matric_number', 'department', 'full_name', 'age', 'level', 'birthdate', 'gender', 'state_of_origin', 'course_pack']
        })
    ]


class LecturerInline(admin.StackedInline):
    model = Lecturer

class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "full_name", "account_type"]
    list_display_links = ["email"]
    list_filter = ['account_type']
    date_hierarchy = 'date_joined'

    fieldsets = [
         (
             "Account Settings", {
                 'fields':['account_type','is_staff', 'is_active', 'groups']
             }
         ),
         (
             "Authentication", {
                 'fields': ['email', 'password']
             }
         ),
         (
             'Basic Info', {
                 'fields': ['last_name', 'first_name', 'middle_name']
             }
         )
     ]

    search_fields = ['last_name', 'first_name', 'middle_name', 'email', 'student__matric_number']
    list_per_page = 25
    

    def view_on_site(self, obj):
        if obj.account_type == 'S':
            student_id = obj.student.id
            url = reverse('student_profile_view', kwargs={'pk':student_id})
            return "http://localhost:8000" + url
        else:
            pass
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj, **kwargs):
        if obj is not None:
            self.readonly_fields = ['password']
            if obj.account_type == 'S':
                self.inlines = [StudentInline]
            elif obj.account_type == 'L':
                self.inlines = [LecturerInline]
        else:
            self.inlines = []
            self.readonly_fields = []

        return super().get_form(request, obj, **kwargs)


custom_admin_site.register(User, UserAdmin)