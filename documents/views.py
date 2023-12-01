from django.shortcuts import render
from django.http import FileResponse, Http404, HttpResponse
from django.conf import settings

from .forms import DocumentUploadForm
from curriculum.models import Course
from documents.models import CourseDocument

import os


def document_upload(request):

    form = DocumentUploadForm()

    context = {"form": form}

    if request.method == "POST":
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("All clear!")
        else:
            print("Whoops. Somehthing went wrong.")

    return render(request, "documents/document_upload.html", context)


def document_view(request, pk):

    material = CourseDocument.objects.get(id=pk)

    document_path = os.path.join(settings.MEDIA_ROOT, material.file.name)

    return FileResponse(open(document_path, "rb"), content_type="application/pdf")


def documents_view(request, code):
    course = Course.objects.get(code=code)
    materials = course.coursedocument_set.all()

    context = {"materials": materials}

    return render(request, "documents/documents_view.html", context)


def document_download(request, pk):
    document = CourseDocument.objects.get(id=pk)

    return FileResponse(document.file, as_attachment=True)
