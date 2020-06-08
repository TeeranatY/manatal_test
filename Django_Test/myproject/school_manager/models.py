from django.db import models

# Create your models here.

class Student(models.Model) :
    student_ID = models.CharField(max_length=20,primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    

class School(models.Model) :
    school_name = models.CharField(max_length=20,primary_key=True)
    max_student_number = models.IntegerField()

class Student_School(models.Model) :
    student_ID = models.ForeignKey("Student",on_delete=models.CASCADE)
    school_name= models.ForeignKey("School",on_delete=models.CASCADE)
    
