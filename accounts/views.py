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
                profile_pk = StudentProfile.objects.get(user=request.user).id
                return redirect('s_profile', pk=profile_pk)
            elif user.account_type == 'TEACHER':
                auth.login(request, user)
                profile_pk = TeacherProfile.objects.get(user=request.user).id
                return redirect('t_profile', pk=profile_pk)
            else:
                messages.error(request, "Access denied {}".format(user.email))
        else:
            messages.error(request, "Invalid Credentials.")
            return redirect('login')

    return render(request, 'accounts/login.html')


def student_profile(request, pk):

    student_user = StudentProfile.objects.get(id=pk)

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=student_user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Saved.")
        else:
            messages.error(request, "Invalid Input.")
    else:
        form = StudentProfileForm(instance=student_user)
    

    context = {
        "form": form
        }

    return render(request, 'accounts/student_profile.html', context)


def teacher_profile(request, pk):

    teacher_user = TeacherProfile.objects.get(id=pk)

    if request.method == 'POST':
        form = TeacherProfileForm(request.POST, instance=teacher_user)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, "Invalid input.")
    else:
        form = TeacherProfileForm(instance=teacher_form)

    context = {"form": form}

    return render(request, 'accounts/teacher_profile.html', context)