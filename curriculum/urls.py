from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_curriculum, name="index_curriculum"),
    path("<slug:course_slug>", views.course_page, name="course_page"),
]
