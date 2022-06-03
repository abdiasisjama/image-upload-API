from dataclasses import fields
from rest_framework import serializers
from .models import Student, StudentImage

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class StudentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentImage
        fields = ['id', 'image']
