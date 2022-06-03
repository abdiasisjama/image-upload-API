from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student, StudentImage
from .serializers import StudentSerializer, StudentImageSerializer

# Create your views here.
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentImageViewSet(ModelViewSet):
    serializer_class = StudentImageSerializer
    def get_queryset(self):
        return StudentImage.objects.filter(student_id = self.kwargs['student_pk'])