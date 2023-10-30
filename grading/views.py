from django.shortcuts import render
from django.http import JsonResponse

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
    print(code)
    context = {}

    try:
        course = Course.objects.get(code=code)

        context.update({"course": course})

    except Exception as e:
        print("Weird, ", e)
        print(f"No course with code {code} exists.")

    return render(request, "grading/course_grading_input.html", context)


def save_student_course_grade(request):
    print(request.body)
    return JsonResponse("You try", safe=False)