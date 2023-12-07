from django.contrib import admin

from .models import StudentAttendance
from core.admin import custom_admin_site


@admin.register(StudentAttendance)
class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ["student", "status", "date"]
    list_display_links = ["student"]


custom_admin_site.register(StudentAttendance, StudentAttendanceAdmin)
