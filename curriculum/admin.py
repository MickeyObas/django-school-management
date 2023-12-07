from django.contrib import admin

from core.admin import custom_admin_site
from .models import Course, DepartmentLevelCoursePack, CourseScheme


class CourseAdmin(admin.ModelAdmin):
    list_display = ["code", "title"]
    prepopulated_fields = {
        "slug": (
            "code",
            "title",
        )
    }
    ordering = ["code"]


class DepartmentLevelCoursePackAdmin(admin.ModelAdmin):
    list_display = ["department", "level"]
    ordering = ["department", "level"]



class CourseSchemeAdmin(admin.ModelAdmin):
    list_display = ["course", "week_1", "week_2"]
    ordering = ["course__code"]


custom_admin_site.register(Course, CourseAdmin)
custom_admin_site.register(DepartmentLevelCoursePack, DepartmentLevelCoursePackAdmin)
custom_admin_site.register(CourseScheme, CourseSchemeAdmin)
