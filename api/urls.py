from django.urls import path

from . import views

urlpatterns = [
    path('users', views.UserList),
    path('users/register', views.UserRegister),
    path('students', views.StudentList),
    path('students/create', views.StudentCreate),
    path('students/<int:pk>', views.StudentRetrieve),
    path('lecturers', views.LecturerList),
    path('lecturers/<int:pk>', views.LecturerRetrieve)
]