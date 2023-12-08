from django.contrib import admin
from django.utils.translation import ngettext

from .models import CourseGrade
from core.admin import custom_admin_site


class CourseGradeAdmin(admin.ModelAdmin):

    list_display = [
        "student_matric_number",
        "course",
        "c_a_total",
        "exam_total",
        "overall",
        "approved",
    ]

    list_editable = ["approved"]
    search_fields = ["course__title", "student__matric_number"]
    list_filter = ["approved", "student__level", "student__department", "course"]
    list_per_page = 50
    actions = ["approve_course_grade"]

    @admin.action(description="Approve selected Course Grades")
    def approve_course_grade(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(
            request,
            ngettext(
                "%d Course Grade was successfully marked as approved.",
                "%d Course Grades was successfully marked as approved.",
                updated,
            ) % updated,
        )


custom_admin_site.register(CourseGrade, CourseGradeAdmin)
