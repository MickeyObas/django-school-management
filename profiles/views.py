from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import StudentCompleteProfileForm
from .models import Student
from department.models import Department


@login_required(login_url="login")
def student_complete_profile(request):

    try:
        student_object = Student.objects.get(user=request.user)
    except:
        student_object = Student.objects.get(user=1)

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

    return render(request, "profiles/student_profile.html", context)
