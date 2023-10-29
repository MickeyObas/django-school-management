from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_grading, name='index_grading'),
    path('<str:code>', views.course_grading_input, name='course_grading_input'),
    path('<str:code>', views.course_grading, name='course_grading')
]

