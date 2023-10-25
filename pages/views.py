from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from core.decorators import already_logged_in
from profiles.models import Student, Lecturer


@login_required(login_url="login")
def dashboard(request):
    if request.user.account_type == 'L':
        return render(request, "pages/lecturer_dashboard.html")
    else:
        return render(request, "pages/dashboard.html")
    


