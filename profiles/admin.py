from django.contrib import admin

from .models import Student, Lecturer
from core.admin import custom_admin_site


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "matric_number",
        "user",
        "gender",
        "level",
        "department",
        "course_pack",
    ]
    list_display_links = ["user"]
    search_fields = ["user"]
    ordering = ["matric_number"]


class LecturerAdmin(admin.ModelAdmin):
    list_display = ["user", "full_name", "department", "gender"]
    list_display_links = ["user"]


custom_admin_site.register(Lecturer, LecturerAdmin)
custom_admin_site.register(Student, StudentAdmin)

