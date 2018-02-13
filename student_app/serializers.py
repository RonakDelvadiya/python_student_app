from rest_framework import serializers
from student_app.models import *

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        exclude = ('created_date', 'modified_date')


class SchoolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schhool

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ('created_date', 'modified_date')


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
