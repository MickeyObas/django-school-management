from django.contrib import admin

from .models import Department
from core.admin import custom_admin_site


class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        "abbreviation",
        "name",
        "head_of_department",
        "no_of_enrolled_staff",
        "no_of_enrolled_students"
    ]
    search_fields = ['name', 'abbreviation']
    ordering = ['abbreviation']

custom_admin_site.register(Department, DepartmentAdmin)