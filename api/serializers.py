from rest_framework import serializers

from accounts.models import User
from profiles.models import Student, Lecturer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=256, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'password']

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        print(validated_data)
        user = User.objects.create_user(email, password)
        return user


class CourseSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=256)


class StudentSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = [
            'email',
            'profile_picture',
            'first_name',
            'last_name',
            'age',
            'department',
            'courses'
        ]

    def get_age(self, obj):
        return obj.age
    

    
class LecturerSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    courses_taught = CourseSerializer(many=True)
    class Meta:
        model = Lecturer
        fields = [
            'lecturer_id',
            'email',
            'first_name',
            'last_name',
            'age',
            'date_of_hire',
            'courses_taught',
            'teaching_experience'
        ]

    def get_age(self, obj):
        return obj.age