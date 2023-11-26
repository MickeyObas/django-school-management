from django.urls import path

from . import views


urlpatterns = [
    path('upload', views.document_upload, name='document_upload'),
    path('document_view/<int:pk>/', views.document_view, name='document_view'),
    path('documents_view/<str:code>', views.documents_view, name='documents_view'),
    path('document_download/<int:pk>/', views.document_download, name='document_download')
]
