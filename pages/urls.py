from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("profiles/", include("profiles.urls")),
    path("curriculum/", include("curriculum.urls")),
    path("messages/", include("messaging.urls")),
    path("grading/", include("grading.urls")),
    path("records/", include("records.urls")),
    path("attendance/", include("attendance.urls")),
    path("payments/", include("payments.urls")),
    path("students/", views.index_students, name="index_students"),
    path("students/<str:code>", views.course_students, name="students_for_course"),
]
