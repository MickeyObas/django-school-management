from django.contrib import admin

from .models import CourseGrade


@admin.register(CourseGrade)
class CourseGradeAdmin(admin.ModelAdmin):
    list_display = [
        "student_matric_number",
        "course",
        "c_a_total",
        "exam_total",
        "overall",
    ]
