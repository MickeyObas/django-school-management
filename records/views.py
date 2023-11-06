from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required

from accounts.permission_handlers.basic import is_student


@user_passes_test(is_student, login_url="dashboard", redirect_field_name=None)
@login_required(login_url="/login/")
def index_records(request):
    return render(request, "records/index_records.html")
