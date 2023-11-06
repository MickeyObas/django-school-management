def is_student(user):
    return user.is_authenticated and user.account_type == "S"


def is_lecturer(user):
    return user.is_authenticated and user.account_type == "L"
