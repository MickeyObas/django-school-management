from django.contrib import admin

from .models import Course
from department.models import Department

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    


