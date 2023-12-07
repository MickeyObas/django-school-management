from django.contrib import admin

from .models import Department
from core.admin import custom_admin_site


class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "head_of_department",
        "no_of_faculty_members",
    ]


custom_admin_site.register(Department, DepartmentAdmin)