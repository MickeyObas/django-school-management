from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_attendance, name='index_attendance'),
    path('record/<str:code>', views.record_attendance, name='record_attendance')
]