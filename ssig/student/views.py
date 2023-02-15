from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer
# Create your views here.

@api_view()
def student_list(request, roll_no):
    students = get_object_or_404( Student , roll_no = roll_no)
    serializer = StudentSerializer(students)    
    return Response(serializer.data)

@api_view()
def student_all(request):
    queryset = Student.objects.select_related('department_id').all()
    serializer = StudentSerializer(queryset  , many = True)
    return Response(serializer.data)
