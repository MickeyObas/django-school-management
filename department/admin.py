from django.contrib import admin

from .models import Department, CourseRegistrationOfficer
from core.admin import custom_admin_site


class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "abbreviation",
        "name",
        "head_of_department",
        "no_of_enrolled_staff",
        "no_of_enrolled_students",
    ]
    search_fields = ["name", "abbreviation"]
    ordering = ["abbreviation"]


class CourseRegistrationOfficerAdmin(admin.ModelAdmin):
    list_display = ["lecturer", "department", "level"]


custom_admin_site.register(Department, DepartmentAdmin)
custom_admin_site.register(CourseRegistrationOfficer, CourseRegistrationOfficerAdmin)
