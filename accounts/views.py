from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from .models import *
from .forms import CustomUserCreationForm, StudentProfileForm, TeacherProfileForm

# Create your views here.
def student_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email has already been used.")
            return redirect('s_register')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            Student.objects.create_user(email=email, password=password2)
            return redirect('login')
        else:
            messages.error(request, "Passwords don't match. Please try again.")
            return redirect('s_register')
    return render(request, 'accounts/student_register.html')


def teacher_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email has already been used.")
            return redirect('t_register')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            Teacher.objects.create_user(email=email, password=password2)
            return redirect('login')
        else:
            messages.error(request, "Passwords don't match. Please try again.")
            return redirect('t_register')
    return render(request, 'accounts/teacher_register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            if user.account_type == 'STUDENT':
                auth.login(request, user)
                print("Student Logged in.")
                print(request.user.email, request.user.account_type)
                return redirect('s_profile', pk=request.user.id)
            elif user.account_type == 'TEACHER':
                auth.login(request, user)
                print("Teacher Logged in.")
                print(request.user.email)
                print(request.user.email, request.user.account_type)
                return redirect('t_profile', pk=request.user.id)
            else:
                messages.error(request, "Access denied {}".format(user.email))
        else:
            messages.error(request, "Invalid Credentials.")
            return redirect('login')

    return render(request, 'accounts/login.html')


def student_profile(request, pk):

    name = 'Student'
    form = StudentProfileForm()

    context = {
        "form": form,
        "name": name,
    }

    return render(request, 'accounts/student_profile.html', context)


def teacher_profile(request, pk):

    name = 'Teacher'
    form = TeacherProfileForm()
    print(name)

    context = {
        "form": form,
        "name": name,
    }
    

    form = TeacherProfileForm()
    return render(request, 'accounts/teacher_profile.html', context)