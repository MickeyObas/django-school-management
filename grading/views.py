from django.shortcuts import render
from django.http import (
    JsonResponse,
    HttpResponseForbidden,
    Http404,
    HttpResponseBadRequest,
)
from django.contrib.auth.decorators import login_required, user_passes_test

import json

from profiles.models import Student
from curriculum.models import Course
from grading.models import CourseGrade
from accounts.permission_handlers.basic import is_student, is_lecturer

# NOTE For now, any lecturer that takes a course can record grades. Later, however, I must enforce a rule where only certain lecturers of a course are given grading duties.


@user_passes_test(is_lecturer, login_url="dashboard", redirect_field_name=None)
@login_required(login_url="login")
def index_grading(request):

    return render(request, "grading/index_grading.html")


@user_passes_test(is_lecturer, login_url="dashboard", redirect_field_name=None)
@login_required(login_url="login")
def display_course_grades(request, code):

    try:
        course = Course.objects.get(code=code)
    except Course.DoesNotExist:
        return Http404("Whoops. There is no such course.")

    context = {"course": course}

    if course not in request.user.lecturer.courses_taught.all():
        return HttpResponseForbidden("<h1>Begone! You are not allowed here!!</h1>")

    return render(request, "grading/course_grading.html", context)


@user_passes_test(is_lecturer, login_url="dashboard", redirect_field_name=None)
@login_required(login_url="login")
def course_grading_input(request, code):

    context = {}

    try:
        course = Course.objects.get(code=code)
        context.update({"course": course})
    except Course.DoesNotExist:
        return Http404("Error 404. There is no such course")

    if course not in request.user.lecturer.courses_taught.all():
        return HttpResponseForbidden("<h1>Begone! You are not allowed here!!</h1>")

    return render(request, "grading/course_grading_input.html", context)


@user_passes_test(is_lecturer, login_url="dashboard", redirect_field_name=None)
@login_required(login_url="login")
def save_student_course_grade(request):

    data = json.loads(request.body)

    matric_number = data["matric_number"]
    course_code = data["course_code"]
    ca_score = data["ca_score"]
    exam_score = data["exam_score"]

    ca_score = int(ca_score)
    exam_score = int(exam_score)

    if ca_score > 40 or exam_score > 60:
        return HttpResponseBadRequest("Attempt to input invalid scores rejected.")

    course = Course.objects.get(code=course_code)

    if course not in request.user.lecturer.courses_taught.all():
        return HttpResponseForbidden("Begone! You cannot perform this action!")

    student = Student.objects.get(matric_number=matric_number)

    student_course_grade = CourseGrade.objects.get(student=student, course=course)
    student_course_grade.c_a_total = ca_score
    student_course_grade.exam_total = exam_score
    student_course_grade.is_default = False
    student_course_grade.save()

    total_score = ca_score + exam_score

    return JsonResponse({"status": "success", "total_score": total_score})


@user_passes_test(is_student, login_url="dashboard", redirect_field_name=None)
@login_required(login_url="login")
def student_grades_view(request):

    student = Student.objects.get(user=request.user)
    grades = CourseGrade.objects.filter(student=student)

    context = {"grades": grades}

    return render(request, "grading/student_grades_view.html", context)
