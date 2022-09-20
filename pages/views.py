from django.shortcuts import render
from core.decorators import already_logged_in
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    return render(request, 'pages/index.html')