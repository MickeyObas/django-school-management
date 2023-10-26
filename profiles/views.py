from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import StudentCompleteProfileForm, LecturerCompleteProfileForm
from .models import Student, Lecturer
from department.models import Department


@login_required(login_url="login")
def student_complete_profile(request):

    student_object = get_object_or_404(Student, user=request.user)

    if request.method == "POST":
        form = StudentCompleteProfileForm(request.POST, request.FILES)
        if form.is_valid():
            student_object.birthdate = form.cleaned_data["birthdate"]
            student_object.state_of_origin = form.cleaned_data["state_of_origin"]
            student_object.gender = form.cleaned_data["gender"]
            department_selected = Department.objects.get(
                abbreviation=form.cleaned_data["department"]
            )
            student_object.department = department_selected
            student_object.profile_picture = request.FILES["profile_picture"]
            student_object.save()
            return redirect("dashboard")
        else:
            messages.error(request, "An error occured whilst filling the form")

    else:

        initial_data = {
            "first_name": student_object.user.first_name,
            "last_name": student_object.user.last_name,
            "middle_name": student_object.user.middle_name,
            "department": student_object.department,
            "level": student_object.level,
        }

        form = StudentCompleteProfileForm(initial=initial_data)

    context = {"form": form}

    return render(request, "profiles/student_complete_profile.html", context)


@login_required(login_url="login")
def lecturer_complete_profile(request):

    lecturer_object = get_object_or_404(Lecturer, user=request.user)

    if request.method == "POST":
        form = LecturerCompleteProfileForm(request.POST, request.FILES)
        if form.is_valid():
            lecturer_object.birthdate = form.cleaned_data["birthdate"]
            lecturer_object.state_of_origin = form.cleaned_data["state_of_origin"]
            lecturer_object.gender = form.cleaned_data["gender"]
            department_selected = Department.objects.get(
                abbreviation=form.cleaned_data["department"]
            )
            lecturer_object.department = department_selected
            lecturer_object.profile_picture = request.FILES["profile_picture"]
            lecturer_object.save()
            return redirect("dashboard")
        else:
            messages.error(request, "An error occured whilst filling the form")

    else:

        initial_data = {
            "first_name": lecturer_object.user.first_name,
            "last_name": lecturer_object.user.last_name,
            "middle_name": lecturer_object.user.middle_name,
            "department": lecturer_object.department,
        }

        form = LecturerCompleteProfileForm(initial=initial_data)

    context = {"form": form}

    return render(request, "profiles/student_profile.html", context)


def student_profile_view(request, pk):

    student = Student.objects.get(id=pk)

    context = {"student": student}

    return render(request, "profiles/student_profile_view.html", context)
