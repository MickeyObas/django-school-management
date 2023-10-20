from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import StudentProfileFormm


@login_required(login_url='login')
def student_profile(request):
    
    form = StudentProfileFormm()

    context = {
        'form': form
    }

    return render(request, 'profiles/student_profile.html', context)
