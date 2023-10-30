from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_messages, name='index_messages'),
    path('message/<int:pk>', views.view_message, name='view_message')
]