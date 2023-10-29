from .models import CourseGrade
from profiles.models import Student

def get_student_ca(student, course):
    course_grade_object = CourseGrade.objects.get(student=student, course=course)
    c_a_score = course_grade_object.c_a_total
    return c_a_score


