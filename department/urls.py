from django.urls import path

from . import views


urlpatterns = [path("courses_approval", views.courses_approval, name="course_approval")]
