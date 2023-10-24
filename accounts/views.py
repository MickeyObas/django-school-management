from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from .models import *
from core.decorators import already_logged_in
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


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
                return redirect("student_complete_profile")
        else:
            return messages.error(request, "Invalid credentials.")

    return render(request, "accounts/login.html")


@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect("login")


def already_logged_in(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("login")
