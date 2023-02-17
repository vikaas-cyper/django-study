from django.db import models
from student.models import Department
# Create your models here.

class Designation(models.Model):
    designation = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Faculty(models.Model):
    name = models.CharField(max_length=200)
    faculty_id = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    mobile_number = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
