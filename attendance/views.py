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
