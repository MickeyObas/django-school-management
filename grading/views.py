from django.shortcuts import render

from curriculum.models import Course

def index_grading(request):

    return render(request, "grading/index_grading.html")


def course_grading(request, code):

    course = Course.objects.get(code=code)
    # course_grades = Course.objects.filter(course=course)

    context = {
        "course": course
    }

    return render(request, "grading/course_grading.html", context)


def course_grading_input(request, code):

    course = Course.objects.get(code=code)

    context = {
        "course": course
    }

    return render(request, "grading/course_grading_input.html", context)