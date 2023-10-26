from curriculum.models import DepartmentLevelCoursePack

def get_student_pack(student):
    student_level = student.level
    student_dept = student.department
    proper_course_pack = DepartmentLevelCoursePack.objects.get(department=student_dept, level=student_level)
    return proper_course_pack
