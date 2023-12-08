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
        "approved"
    ]
    list_editable = ['approved']
    search_fields  = ['course__title', 'student__matric_number']
    list_filter = ['approved', 'student__level', 'course']
    list_per_page = 50



custom_admin_site.register(CourseGrade, CourseGradeAdmin)