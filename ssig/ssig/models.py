from django.db import models
from student.models import Student
from faculty.models import Faculty

# Create your models here.

class Ssig(models.Model):
    
    ssig_number = models.CharField(max_length = 30)
    faculty = models.ForeignKey(Faculty , on_delete=models.CASCADE)
    student = models.ForeignKey(Student , on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    