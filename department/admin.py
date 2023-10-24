from django.contrib import admin

from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "head_of_department",
        "no_of_faculty_members",
    ]
