from rest_framework import serializers
from . import models

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ['id', 'name', 'code']
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'name', 'roll_no', 'department']
    