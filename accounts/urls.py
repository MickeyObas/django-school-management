from django.urls import path, include
from . import views

urlpatterns = [
    path('register/student/', views.student_register, name='s_register'),
    path('register/teacher', views.teacher_register, name='t_register'),

    path('login/', views.login, name='login'),

    path('profile/student/<str:pk>', views.student_profile, name='s_profile'),
    path('profile/teacher/<str:pk>', views.teacher_profile, name='t_profile')
]