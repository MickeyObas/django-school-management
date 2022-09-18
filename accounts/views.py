from django.shortcuts import render
from .forms import CustomUserCreationForm, StudentProfileForm

# Create your views here.
def register(request):
    form = StudentProfileForm()
    return render(request, 'accounts/register.html', {'form': form})