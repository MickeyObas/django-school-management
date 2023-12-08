from django.contrib import admin

from core.admin import custom_admin_site
from .models import Course, DepartmentLevelCoursePack, CourseScheme


class CourseCodePrefixFilter(admin.SimpleListFilter):
    title = 'course_code_prefix'
    parameter_name = 'course_code_prefix'

    def lookups(self, request, model_admin):
        course_code_prefixs = set([course.course_code_prefix for course in model_admin.model.objects.all()])
        return [(course_code_prefix, course_code_prefix) for course_code_prefix in course_code_prefixs]
    
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(code__icontains=self.value())


class CourseAdmin(admin.ModelAdmin):
    list_filter = [CourseCodePrefixFilter, 'no_of_units']
    list_display = ["code", "title", "no_of_units"]
    prepopulated_fields = {
        "slug": (
            "code",
            "title",
        )
    }
    ordering = ["code"]

class DepartmentLevelCoursePackAdmin(admin.ModelAdmin):
    list_display = ["department", "level", "courses_list"]
    readonly_fields = ['courses_list']
    ordering = ["department", "level"]
    filter_horizontal  = ['courses']

    def courses_list(self, obj):
        course_code_list = []
        for course in obj.courses.all():
            course_code_list .append(course.code)
        return course_code_list

class CourseSchemeAdmin(admin.ModelAdmin):
    list_display = ["course", "week_1", "week_2", "week_3"]
    ordering = ["course__code"]


custom_admin_site.register(Course, CourseAdmin)
custom_admin_site.register(DepartmentLevelCoursePack, DepartmentLevelCoursePackAdmin)
custom_admin_site.register(CourseScheme, CourseSchemeAdmin)
