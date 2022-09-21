from django.shortcuts import render
from core.decorators import already_logged_in
from accounts.models import StudentProfile, TeacherProfile
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):

    student_user = StudentProfile.objects.filter(user=request.user).exists()
    teacher_user = TeacherProfile.objects.filter(user=request.user).exists()

    context = {
        "student_user":student_user,
        "teacher_user": teacher_user,
    }

    return render(request, 'pages/index.html', context)