from rest_framework import serializers
from  school_manager.models import School,Student,Student_School




class student_serializer(serializers.ModelSerializer):
    class Meta :
        model = Student 
        fields = ("student_ID","firstname","lastname")

class school_serializer(serializers.ModelSerializer):
    class Meta :
        model = School
        fields = ("school_name","max_student_number")

class ss_serializer(serializers.ModelSerializer) :
    class Meta :
        model = Student_School
        fields=("student_ID","school_name")