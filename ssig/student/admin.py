from django.contrib import admin

from . import models

# Register your models here.

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll_no']


@admin.register(models.Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ['batch']
    ordering = ['batch']

@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'department_code']
    @admin.display(ordering=['name'])
    def department_code(self, department):
        return department.code
    
    
# admin.site.register(models.Department)
