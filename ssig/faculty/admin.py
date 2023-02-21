from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty_id', 'department' , 'designation']


@admin.register(models.Designation)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['designation']
