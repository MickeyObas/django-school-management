from rest_framework import generics, exceptions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from profiles.models import Student, Lecturer
from api.serializers import (
    UserSerializer,
    StudentSerializer,
    LecturerSerializer
)

class UserRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

UserRegister = UserRegisterView.as_view()

class StudentCreateView(APIView):
    # Associates a user with a brand new Student profile
    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

StudentCreate = StudentCreateView.as_view()

class UserListView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

UserList = UserListView.as_view()

class StudentListView(APIView):
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

StudentList = StudentListView.as_view()

class StudentRetrieveView(APIView):
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            pk = kwargs.get('pk')
            try:
                student = Student.objects.get(id=pk)
                serializer = StudentSerializer(student)
            except:
                raise exceptions.NotFound(detail=f"Student with ID: {pk} does not exist.")
            return Response(serializer.data)
    
StudentRetrieve = StudentRetrieveView.as_view()

class LecturerListView(APIView):
    def get(self, request, *args, **kwargs):
        lecturers = Lecturer.objects.all()
        serializer = LecturerSerializer(lecturers, many=True)
        return Response(serializer.data)
    
LecturerList = LecturerListView.as_view()

class LecturerRetrieveView(APIView):
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            pk = kwargs.get('pk')
            try:
                lecturer = Lecturer.objects.get(id=pk)
                serializer = LecturerSerializer(lecturer)
            except:
                raise exceptions.NotFound(detail=f"Lecturer with id: {pk} does not exist.")
            return Response(serializer.data)

LecturerRetrieve = LecturerRetrieveView.as_view()