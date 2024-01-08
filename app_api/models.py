from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    roll_num=models.IntegerField()
    subject=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
