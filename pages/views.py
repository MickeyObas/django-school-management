from django.shortcuts import render, get_object_or_404
from core.decorators import already_logged_in
from profiles.models import Student, Lecturer
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def dashboard(request):
    return render(request, "pages/dashboard.html")

