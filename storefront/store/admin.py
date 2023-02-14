from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price']
    list_editable = ['unit_price']


admin.site.register(models.Collection)

# admin.site.register(models.Product)
