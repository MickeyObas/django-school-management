from django.shortcuts import render

from .models import StudentAttendance
from profiles.models import Student
from curriculum.models import Course


def index_attendance(request):
    return render(request, "attendance/index_attendance.html")

def record_attendance(request, code):

    course = Course.objects.get(code=code)

    context = {
        "course": course
    }

    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('attendance_'):
                student_id = key.split('_')[-1]
                status = value
                print(status)
                student = Student.objects.get(id=student_id)
                StudentAttendance.objects.create(student=student, status=value)

    return render(request, "attendance/record_attendance.html", context)


def student_attendance_view(request):

    student_object = Student.objects.get(user=request.user)

    student_attendance_records = StudentAttendance.objects.filter(student=student_object)

    print(student_attendance_records)

    context = {
        "student_attendance_records": student_attendance_records
    }

    return render(request, "attendance/student_attendance_view.html", context)
