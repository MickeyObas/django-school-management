from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import user_passes_test, login_required

from .models import StudentAttendance
from profiles.models import Student
from curriculum.models import Course
from accounts.permission_handlers.basic import is_lecturer

from dateutil import parser


@user_passes_test(is_lecturer, login_url="dashboard")
def index_attendance(request):
    return render(request, "attendance/index_attendance.html")


@user_passes_test(is_lecturer, login_url="dashboard", redirect_field_name=None)
@login_required(login_url="login")
def record_attendance(request, code):

    course = Course.objects.get(code=code)

    context = {"course": course}

    if course not in request.user.lecturer.courses_taught.all():
        return HttpResponseForbidden("You are not allowed here. Be gone!")

    if request.method == "POST":
        for key, value in request.POST.items():
            if key.startswith("attendance_"):
                student_id = key.split("_")[-1]
                status = value
                print(status)
                student = Student.objects.get(id=student_id)
                StudentAttendance.objects.create(student=student, status=value, course=course)

    return render(request, "attendance/record_attendance.html", context)


@login_required(login_url="login")
def student_attendance_view(request):

    course_query = request.GET.get('course', '')
    status_query = request.GET.get('status', '')
    student_object = Student.objects.get(user=request.user)

    query = Q()

    if course_query:
        query &=  Q(course__code__exact=course_query)

    if status_query:
        query &= Q(status__iexact=status_query)

    student_attendance_records = StudentAttendance.objects.filter(student=student_object).filter(query)

    context = {
        "student_attendance_records": student_attendance_records,
        "student_object": student_object
        }

    return render(request, "attendance/student_attendance_view.html", context)
