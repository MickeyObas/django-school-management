from django.shortcuts import render, get_object_or_404

from .models import Course


def index_curriculum(request):
    return render(request, "pages/index_curriculum.html")

def course_page(request, course_slug):

    course = get_object_or_404(Course, slug=course_slug)

    context = {
        "course": course
    }

    return render(request, 'curriculum/course_page.html', context)
