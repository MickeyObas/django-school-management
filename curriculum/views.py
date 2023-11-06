from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Course
from accounts.permission_handlers.basic import is_student


@user_passes_test(is_student, login_url="dashboard", redirect_field_name=None)
@login_required(login_url="login")
def index_curriculum(request):
    return render(request, "pages/index_curriculum.html")


@login_required(login_url="login")
def course_page(request, course_slug):

    course = get_object_or_404(Course, slug=course_slug)

    context = {"course": course}

    return render(request, "curriculum/course_page.html", context)
