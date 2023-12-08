from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Course
from grading.signals import student_courses_registration_complete
from profiles.models import Student
from accounts.permission_handlers.basic import is_student

import json


@user_passes_test(is_student, login_url="dashboard", redirect_field_name=None)
@login_required(login_url="login")
def index_curriculum(request):
    return render(request, "pages/index_curriculum.html")


@login_required(login_url="login")
def course_page(request, course_slug):

    course = get_object_or_404(Course, slug=course_slug)

    context = {"course": course}

    return render(request, "curriculum/course_page.html", context)


@login_required(login_url="login")
def course_registration(request):
    return render(request, "curriculum/course_registration.html")


@login_required(login_url="login")
def register_courses(request):
    if request.method == "POST":
        if request.user.student.has_registered_courses:
            return JsonResponse(
                {
                    "status": "failure",
                    "message": "You have already registered your courses for this semester.",
                }
            )
        else:
            data = json.loads(request.body)
            student_id = data["student-id"]
            student = Student.objects.get(id=student_id)
            student.has_registered_courses = True
            student.save()
            assert request.user.student.id == int(student_id), "Student ID Inconsistent"
            student_courses_registration_complete.send(
                sender="register_courses", student_id=student_id
            )

            return JsonResponse(
                {"status": "success", "message": "Courses registered successfully."}
            )
