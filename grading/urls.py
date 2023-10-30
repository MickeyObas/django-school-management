from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_grading, name='index_grading'),
    path('record/<str:code>', views.course_grading_input, name='course_grading_input'),
    path('display-course-grades/<str:code>', views.display_course_grades, name='display_course_grades'),
    path('save_student_course_grade', views.save_student_course_grade, name='save_student_course_grade')
]

