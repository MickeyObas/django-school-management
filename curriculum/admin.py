from django.contrib import admin

from .models import Course, DepartmentLevelCoursePack, CourseScheme


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["code", "title"]
    prepopulated_fields = {
        "slug": (
            "code",
            "title",
        )
    }
    ordering = ["code"]


@admin.register(DepartmentLevelCoursePack)
class DepartmentLevelCoursePackAdmin(admin.ModelAdmin):
    list_display = ["department", "level"]
    ordering = ["department", "level"]


@admin.register(CourseScheme)
class CourseSchemeAdmin(admin.ModelAdmin):
    list_display = ['course', 'week_1', 'week_2']
    ordering = ['course__code']
