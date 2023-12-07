from django.contrib import admin

from .models import CourseGrade
from core.admin import custom_admin_site

class CourseGradeAdmin(admin.ModelAdmin):
    list_display = [
        "student_matric_number",
        "course",
        "c_a_total",
        "exam_total",
        "overall",
    ]

custom_admin_site.register(CourseGrade, CourseGradeAdmin)