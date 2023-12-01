from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_curriculum, name="index_curriculum"),
    path("course/<slug:course_slug>", views.course_page, name="course_page"),
    path("course_registration", views.course_registration, name="course_registration"),
    path("register_courses", views.register_courses, name="register_courses"),
]
