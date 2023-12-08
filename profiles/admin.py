from django.contrib import admin

from .models import Student, Lecturer
from core.admin import custom_admin_site


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "matric_number",
        'full_name',
        "user",
        "gender",
        "level",
        "department",
        "course_pack",
    ]
    list_display_links = ["matric_number"]
    search_fields = ["matric_number", "user__email", "user__first_name", "user__last_name", "user__middle_name", "user__id"]
    ordering = ["matric_number"]
    list_filter = ['department', 'gender', 'level']
    list_per_page = 50
    

class LecturerAdmin(admin.ModelAdmin):
    search_fields = ['lecturer_id', 'user__email', 'user__first_name', 'user__last_name']
    list_display = ["lecturer_id", "user", "full_name", "department", "gender"]
    list_display_links = ["user"]
    list_filter = ["department", "gender"]


custom_admin_site.register(Lecturer, LecturerAdmin)
custom_admin_site.register(Student, StudentAdmin)

