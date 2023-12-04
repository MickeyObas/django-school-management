from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import FileResponse, Http404, HttpResponse

from core import renderers
from profiles.models import Student
from curriculum.models import Course
from .forms import DocumentUploadForm
from grading.models import CourseGrade
from documents.models import CourseDocument
from accounts.permission_handlers.basic import is_student, is_lecturer

import os


@user_passes_test(is_lecturer, login_url='dashboard', redirect_field_name=None)
@login_required(login_url='login')
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


@login_required(login_url='login')
def document_view(request, pk):

    material = CourseDocument.objects.get(id=pk)

    document_path = os.path.join(settings.MEDIA_ROOT, material.file.name)

    return FileResponse(open(document_path, "rb"), content_type="application/pdf")


@login_required(login_url='login')
def documents_view(request, code):
    course = Course.objects.get(code=code)
    materials = course.coursedocument_set.all()

    context = {"materials": materials}

    return render(request, "documents/documents_view.html", context)


@login_required(login_url='login')
def document_download(request, pk):
    document = CourseDocument.objects.get(id=pk)

    return FileResponse(document.file, as_attachment=True)


@login_required(login_url='login')
def result_pdf_view(request, *args, **kwargs):
    student = Student.objects.get(user=request.user)
    grades = CourseGrade.objects.filter(student=student)

    data = {
        'grades': grades,
        'student': student
        }

    response = renderers.render_to_pdf('documents/result-template.html', data)

    if response.status_code == 404:
        raise Http404("Result not found")
    
    filename = f"Result_Sheet_{student.full_name}.pdf"
    
    content = f"attachment; filename={filename}"
    response["Content-Disposition"] = content
    return response