def is_lecturer(user):
    return user.is_authenticated and user.account_type == 'L'

def is_lecturer_and_teaches_course(user, course_code):
    return is_lecturer(user) and course_code