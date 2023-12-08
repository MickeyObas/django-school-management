from django.dispatch import Signal, receiver

from profiles.models import Student
from grading.models import CourseGrade


student_courses_registration_complete = Signal()


@receiver(student_courses_registration_complete)
def create_registered_student_course_records(sender, student_id, **kwargs):
    registered_student = Student.objects.get(id=student_id)
    registered_student_courses = registered_student.course_pack.courses.all()
    for course in registered_student_courses:
        CourseGrade.objects.create(student=registered_student, course=course)
