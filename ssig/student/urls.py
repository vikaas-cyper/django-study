from django.urls import path 
from . import views


urlpatterns = [
     path('students/<int:id>', views.student_list),
     path('students/', views.StudentList.as_view()),
     
]
