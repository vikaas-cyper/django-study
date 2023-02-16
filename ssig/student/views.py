from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer
# Create your views here.

class StudentList(APIView):
    def get(self , request):
        queryset = Student.objects.select_related('department').all()
        serializer = StudentSerializer(queryset  , many = True)
        return Response(serializer.data)
    
    def post(self , request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view([ 'GET','PUT', 'DELETE'])
def student_list(request, id):
    student = get_object_or_404(Student, pk =id )
    if request.method == "GET":
        serializer = StudentSerializer(student)    
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    