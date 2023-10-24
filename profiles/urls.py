from django.urls import path

from . import views

urlpatterns = [
    path(
        "student_complete_profile",
        views.student_complete_profile,
        name="student_complete_profile",
    )
]
