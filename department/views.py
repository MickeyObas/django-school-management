from django.shortcuts import render
from django.forms import modelformset_factory
from django.http import HttpResponseForbidden

from .models import CourseRegistrationOfficer
from profiles.models import Student, Lecturer
from .forms import ApproveStudentsCoursesForm


def courses_approval(request):

    if request.user.lecturer.id not in list(
        CourseRegistrationOfficer.objects.all().values_list("lecturer_id", flat=True)
    ):
        return HttpResponseForbidden("You are not a registration officer. Begone!!!")

    course_registration_officer_profile = CourseRegistrationOfficer.objects.get(
        lecturer=request.user.lecturer
    )

    students = Student.objects.filter(
        department=course_registration_officer_profile.department,
        level=course_registration_officer_profile.level,
    ).order_by("courses_approved")

    ApproveStudentsCoursesFormset = modelformset_factory(
        Student, form=ApproveStudentsCoursesForm, extra=0
    )

    if request.method == "POST":
        formset = ApproveStudentsCoursesFormset(request.POST, queryset=students)
        if formset.is_valid():
            formset.save()
            print("Yeah, we good!")
        else:
            for form in formset:
                print(form.errors)
    else:
        formset = ApproveStudentsCoursesFormset(queryset=students)

    context = {"formset": formset}

    return render(request, "department/courses_approval.html", context)
