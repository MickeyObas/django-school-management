from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("profiles/", include("profiles.urls")),
    path("curriculum/", include("curriculum.urls")),
    path("messages/", include("messaging.urls")),
    path("students", views.index_students, name="index_students"),
    path("students/<str:code>", views.students_for_course, name="students_for_course"),
]
