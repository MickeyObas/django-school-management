from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CustomUserCreationForm
from .decorators import already_logged_in


@already_logged_in
def register(request):

    # FIXME New user can reigister without name values and password strength checks. Also add email confirmation. Extremely important.

    if request.method == "POST":
        account_type = request.POST.get("account_type")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        middle_name = request.POST.get("middle_name")
        email = request.POST.get("email").lower()
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "The passwords don't match.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists.")
            return redirect("register")

        new_user = User.objects.create_user(
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            account_type=account_type,
        )
        return redirect("login")

    else:
        return render(request, "accounts/register.html")


@already_logged_in
def login(request):
    if request.method == "POST":
        email = request.POST.get("email").lower()
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
