from django.shortcuts import render

def index_records(request):
    return render(request, "records/index_records.html")