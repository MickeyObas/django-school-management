from django.contrib import admin

from .models import StudentAttendance
from core.admin import custom_admin_site

from datetime import date


@admin.register(StudentAttendance)
class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ["matric_number", "course", "status", "date", "comment"]
    list_display_links = ["matric_number"]
    list_filter = ["status", "course", "student__department"]
    search_fields = ["matric_number", "course", "date"]
    ordering = ["date"]
    date_hierarchy = "date"


custom_admin_site.register(StudentAttendance, StudentAttendanceAdmin)
