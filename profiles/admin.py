from django.contrib import admin

from .models import Student, Lecturer


@admin.register(Student)
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


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ["user", "full_name", "department", "gender"]
    list_display_links = ["user"]
