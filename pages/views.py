from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required

from curriculum.models import Course
from profiles.models import Student, Lecturer
from core.decorators import already_logged_in
from accounts.permission_handlers.basic import is_lecturer


@login_required(login_url="login")
def dashboard(request):
    if request.user.account_type == "L":
        return render(request, "pages/index_lecturer_dashboard.html")
    else:
        return render(request, "pages/index_student_dashboard.html")


@user_passes_test(is_lecturer, login_url="dashboard", redirect_field_name=None)
@login_required(login_url="login")
def index_students(request):
    return render(request, "pages/index_students.html")


@user_passes_test(is_lecturer, login_url="dashboard", redirect_field_name=None)
@login_required(login_url="login")
def course_students(request, code):

    course = Course.objects.get(code=code)

    context = {"course": course}

    return render(request, "curriculum/course_students.html", context)
