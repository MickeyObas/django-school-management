from django import forms
from django.urls import path
from django.db.models import Q
from django.contrib import admin
from django.urls.resolvers import URLPattern
from django.template.response import TemplateResponse

from .models import Student, Lecturer
from department.models import Department
from core.admin import custom_admin_site
from .forms import ApproveCoursesAdminForm


CourseApproveFormSet = forms.modelformset_factory(
    Student,
    fields=["matric_number", "department", "level", "courses_approved"],
    extra=0,
    form=ApproveCoursesAdminForm,
)


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "matric_number",
        "full_name",
        "user",
        "gender",
        "level",
        "department",
        "course_pack",
    ]
    list_display_links = ["matric_number"]
    search_fields = [
        "matric_number",
        "user__email",
        "user__first_name",
        "user__last_name",
        "user__middle_name",
        "user__id",
    ]
    ordering = ["matric_number"]
    list_filter = ["department", "gender", "level"]
    list_per_page = 50

    def get_urls(self) -> list[URLPattern]:
        urls = super().get_urls()
        my_urls = [
            path(
                "approve_courses/<int:dept_pk>/<str:level>",
                self.admin_site.admin_view(self.approve_courses),
            ),
            path(
                "query_students",
                self.admin_site.admin_view(self.query_students),
                name="query_students",
            ),
        ]
        return my_urls + urls

    def query_students(self, request):

        context = dict(self.admin_site.each_context(request))

        return TemplateResponse(
            request, "profiles/query_students_to_approve.html", context
        )

    def approve_courses(self, request, **kwargs):

        """
        if request.method == 'GET':
        level_query = request.GET.get('level', '')
        department_query = request.GET.get('department', '')

        if department_query != '':
            department = Department.objects.filter(Q(name__iexact=department_query) | Q(abbreviation__iexact=department_query)).first()
            students = Student.objects.filter(department=department, level=level_query)
        else:
            students = Student.objects.all()
        """

        dept_id = kwargs.get("dept_pk")
        students_level = kwargs.get("level")

        department = Department.objects.get(id=dept_id)
        students = Student.objects.filter(department=department, level=students_level)

        if request.method == "GET":
            formset = CourseApproveFormSet(queryset=students)
        else:
            formset = CourseApproveFormSet(request.POST, queryset=students)
            if formset.is_valid():
                formset.save()
                print("Yeah Nigga!")
            else:
                print(formset.errors)
                print("Nope lol")

        context = dict(self.admin_site.each_context(request))

        context.update({"formset": formset})

        return TemplateResponse(request, "profiles/approve_courses.html", context)


class LecturerAdmin(admin.ModelAdmin):

    search_fields = [
        "lecturer_id",
        "user__email",
        "user__first_name",
        "user__last_name",
    ]
    list_display = ["lecturer_id", "user", "full_name", "department", "gender"]
    list_display_links = ["user"]
    list_filter = ["department", "gender"]


custom_admin_site.register(Lecturer, LecturerAdmin)
custom_admin_site.register(Student, StudentAdmin)
