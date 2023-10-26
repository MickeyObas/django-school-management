from django.core.management.base import BaseCommand

import random
from faker import Faker

from ...models import User
from profiles.models import Student
from profiles.forms import StudentCompleteProfileForm
from curriculum.utils import get_student_pack
from department.models import Department


class Command(BaseCommand):
    help = 'Populate students with fake data'

    DEPARTMENTS = [
        'CSC',
        'BMT',
        'SEN'
    ]

    GENDERS = [
        'M',
        'F'
    ]

    def handle(self, *args, **kwargs):

        fake = Faker()

        for _ in range(30):
            user = User.objects.create_user(
                email=fake.email(),
                password='Harobed20010420',
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                middle_name = fake.first_name(),
                account_type = 'S'
            )

            student_profile = Student.objects.get(user=user)
            student_profile.gender = random.choice(Command.GENDERS)
            abbr = random.choice(Command.DEPARTMENTS)
            student_profile.department = Department.objects.get(abbreviation=abbr)
            student_profile.save()
            student_profile.course_pack = get_student_pack(student_profile)
            student_profile.save()
            

        # TODO Assert that this handle triggers the create_student_profile signal

        self.stdout.write(self.style.SUCCESS('Sucessfully populated students.'))