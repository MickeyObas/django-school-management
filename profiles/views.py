from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import StudentProfileFormm, StudentDisplayForm
from .models import Student


@login_required(login_url='login')
def student_profile(request):

    try:
        student_object = Student.objects.get(user=request.user)
    except:
        student_object = Student.objects.get(user=1)

    if request.method == 'POST':
        pass

    else:

        initial_data = {
            'first_name': student_object.user.first_name,
            'last_name': student_object.user.last_name,
            'middle_name': student_object.user.middle_name,
            'department': student_object.department,
            'level': student_object.level
        }

        form = StudentDisplayForm(initial=initial_data)

    context = {
        'form': form
    }

    return render(request, 'profiles/student_profile.html', context)
