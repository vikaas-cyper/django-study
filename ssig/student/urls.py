from django.urls import path 
from . import views


urlpatterns = [
     path('students/', views.student_all),
     path('students/<roll_no>', views.student_list),
     
]
