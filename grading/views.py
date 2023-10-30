from django.shortcuts import render
from django.http import JsonResponse

import json

from profiles.models import Student
from curriculum.models import Course
from grading.models import CourseGrade

def index_grading(request):

    return render(request, "grading/index_grading.html")


def display_course_grades(request, code):

    course = Course.objects.get(code=code)


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

    data = json.loads(request.body)

    print(data)

    matric_number = data['matric_number']
    course_code = data['course_code']
    ca_score = data['ca_score']
    exam_score = data['exam_score']

    student = Student.objects.get(matric_number=matric_number)
    course = Course.objects.get(code=course_code)

    student_course_grade = CourseGrade.objects.get(student=student, course=course)
    student_course_grade.c_a_total = ca_score
    student_course_grade.exam_total = exam_score
    student_course_grade.is_default = False
    student_course_grade.save()

    return JsonResponse(f"Student: {matric_number} score for {course} saved.", safe=False)