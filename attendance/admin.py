from django.contrib import admin

from .models import StudentAttendance


@admin.register(StudentAttendance)
class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ["student", "status", "date"]
    list_display_links = ["student"]
