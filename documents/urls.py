from django.urls import path

from . import views


urlpatterns = [
    path('upload', views.document_upload, name='document_upload')
]
