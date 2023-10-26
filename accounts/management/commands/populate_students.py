from django.core.management.base import BaseCommand
from faker import Faker

from models import User
from profiles.models import Student
from profiles.forms import StudentCompleteProfileForm


class Command(BaseCommand):
    help = 'Populate students with fake data'
    
    def handle(self, *args, **kwargs):
        fake = Faker()
        user = User.objects.create_user(
            email=fake.email()
            password='Harobed20010420',
            first_name = fake.first_name()
            last_name = fake.last_name()
            middle_name = fake.middle_name()
            account_type = 'S'
        )

        # TODO Assert that this handle triggers the create_student_profile signal


        self.stdout.write(self.style.SUCCESS('Sucessfully populated students.'))