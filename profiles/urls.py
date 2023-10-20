from django.urls import path

from . import views

urlpatterns = [
    path('student_profile', views.student_profile, name='student_profile')
]