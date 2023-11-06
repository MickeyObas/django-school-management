from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CustomUserCreationForm
from .decorators import already_logged_in


@already_logged_in
def register(request):

    form = CustomUserCreationForm()

    context = {"form": form}

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            print("Bad form.")
            return messages.error(
                request, "Form filled incorrectly. Please do try again."
            )

    return render(request, "accounts/register.html", context)


@already_logged_in
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            auth.login(request, user)
            if not user.first_login:
                return redirect("dashboard")
            else:
                user.first_login = False
                user.save()
                if user.account_type == "S":
                    return redirect("student_complete_profile")
                elif user.account_type == "L":
                    return redirect("lecturer_complete_profile")
                else:
                    raise ValueError("Invalid User Type")
        else:
            messages.error(request, "Invalid credentials.")
            return redirect("login")

    return render(request, "accounts/login.html")


@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect("login")
