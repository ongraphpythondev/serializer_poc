from django.contrib import admin
from .models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll_num','email','subject','address']
admin.site.register(Student,StudentAdmin)