from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_records, name='index_records')
]