from django.shortcuts import render

from .forms import DocumentUploadForm

def document_upload(request):
    
    form = DocumentUploadForm()

    context = {
        "form": form
    }

    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("All clear!")
        else:
            print("Whoops. Somehthing went wrong.")

    return render(request, "documents/document_upload.html", context)
