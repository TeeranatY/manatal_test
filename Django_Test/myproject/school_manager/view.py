from rest_framework import viewsets,status
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from school_manager.Serializers import student_serializer,school_serializer,ss_serializer
from school_manager.models import Student, School , Student_School 
import string,random

class manage_student_withID(APIView) :
    def get_object(self,id=None) :
        try :
            return Student.objects.get(student_ID=id)
        except :
            return False
    def get(self,request,id=None) :
        try :
            obj = self.get_object(id)
            if obj == False : 
                return Response(data="ID is not exist",status=status.HTTP_400_BAD_REQUEST)
            serializer = student_serializer(obj)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except :
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id=None) :
        try :
            instance = Student.objects.get(student_ID=id)
        except :
            return Response("ID is not exist",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        request.data["student_ID"] = id
        print(instance)
        serializer = student_serializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(data="Serializer is not valid",status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self,request,id=None) :
        if id == None :
            return Response(data="Please specific ID",status=status.HTTP_400_BAD_REQUEST)
        try :
            instance = Student.objects.get(student_ID=id)
            instance.delete()
            return Response(data="Delete",status=status.HTTP_200_OK)
        except :
            return Response(data="ID is not valid",status=status.HTTP_400_BAD_REQUEST)

class manage_student(APIView) :

    def get_object(self) :
        try :
            return Student.objects.all()
        except :
            return False
        
    def get(self,request) :
        try :
            serializer = student_serializer(self.get_object(),many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except :
            return  Response("Student is empty!",status=status.HTTP_400_BAD_REQUEST)
        
    def post(self,request) :
        #check if student not already exist
        temp1 = Student.objects.filter(firstname=request.data['firstname'],lastname=request.data['lastname'])
        if temp1.count()!= 0 : # student exist
            return Response(data="This student are already exist!",status=status.HTTP_400_BAD_REQUEST)
        
        #check if school exists
        temp1 = School.objects.filter(school_name=request.data['school_name'])
        if temp1.count()==0 : #school doesn't exist
            return Response(data= "School name does not exist",status=status.HTTP_400_BAD_REQUEST)
        #check if can add student into school
        temp2 = Student_School.objects.filter(school_name=request.data['school_name'])
        print(temp2)
        print("temp2.count() is : " + str(temp2.count()))
        if temp2.count() >= temp1.first().max_student_number :
            return Response(data="Cannot add student anymore",status=status.HTTP_400_BAD_REQUEST)
        request.data['student_ID'] = ''.join(random.choice(string.ascii_letters) for i in range(6))
        
        print(request.data)
        serializer_student = student_serializer(data=request.data)
        if serializer_student.is_valid() :
            serializer_student.save()
        else :
            print("cannot validate student serializer")
            print(serializer_student.errors)
        
        serializer_ss = ss_serializer(data=request.data)
        if serializer_ss.is_valid() :
            serializer_ss.save()
        else : 
            print("cannot validate ss serializer")
            print(serializer_ss.errors)
            return  Response(serializer_ss.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer_student.data,status=status.HTTP_201_CREATED)
        
        
class manage_school(APIView) :

    def get_object(self) :
        try :
            print(School.objects.all())
            return School.objects.all()
        except :
            return False
    
    def get(self,request) :
        
        try :
            serializer = school_serializer(self.get_object(),many=True)
            print("ishere?")
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except  :
            return Response("School is empty!",status=status.HTTP_400_BAD_REQUEST)
        
    def post(self,request) :
        if School.objects.filter(school_name=request.data["school_name"]).count() > 0 :
            return Response("School name already exist",status=status.HTTP_400_BAD_REQUEST)
        
        serializer = school_serializer(data=request.data)
        
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else :
            return Response(data="Serializer is not valid",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class manage_school_withID(APIView) :
    def get_school_object(self,id=None) :
        try :
            return School.objects.get(school_name=id)
        except :
            return False
      
        
    def get(self,request,id=None) :
        try :
            obj = self.get_school_object(id)
            if obj == False : 
                return Response(data="Name is not exist",status=status.HTTP_400_BAD_REQUEST)
            serializer = school_serializer(obj)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except :
            return Response(data="Something wrong",status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id=None) :
        try :
            instance = School.objects.get(school_name=id)
        except :
            return Response("Name is not valid",status=status.HTTP_200_OK)
        request.data['school_name'] = id
        serializer = school_serializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data="Serializer is not valid",status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self,request,id=None) :
        #delete student belong to school
        instance = Student_School.objects.filter(school_name=id)
        for each in instance :
            student = Student.objects.get(student_ID=each.student_ID.student_ID)
            student.delete()

        try :
            instance = School.objects.get(school_name=id)
            instance.delete()
            return Response(data="Delete",status=status.HTTP_200_OK)
        except :
            return Response(data="Name is not valid",status=status.HTTP_400_BAD_REQUEST)


class nested_manage_school(APIView):

    def get_student_object(self,id) :
        query = Student_School.objects.filter(school_name=id)
        out = list()
        print(query)
        for each in query :
            out.append(Student.objects.get(student_ID=each.student_ID.student_ID))
        # print(out)
        return out
    def get(self,request,id=None) :
        #check if school exists
        temp1 = School.objects.filter(school_name=id)
        if temp1.count()==0 : #school doesn't exist
            return Response(data= "School name does not exist",status=status.HTTP_400_BAD_REQUEST)

        serializer = student_serializer(self.get_student_object(id),many=True)
        return Response(data={"student":serializer.data},status=status.HTTP_200_OK)

    def post(self,request,id=None) :
        #check if student not already exist
        temp0 = Student.objects.filter(firstname=request.data['firstname'],lastname=request.data['lastname'])
        if temp0.count()!= 0 : # student exist
            return Response(data="This student are already exist!",status=status.HTTP_400_BAD_REQUEST)

        #check if school exists
        temp1 = School.objects.filter(school_name=id)
        if temp1.count()==0 : #school doesn't exist
            return Response(data= "School name does not exist",status=status.HTTP_400_BAD_REQUEST)

        #check if can add student into school
        temp2 = Student_School.objects.filter(school_name=id)
        print(temp2)
        print("temp2.count() is : " + str(temp2.count()))
        if temp2.count() >= temp1.first().max_student_number :
            return Response(data="Cannot add student anymore",status=status.HTTP_400_BAD_REQUEST)

        request.data['school_name'] = id 
        request.data['student_ID'] = ''.join(random.choice(string.ascii_letters) for i in range(6))
        print(request.data)
        serializer_student = student_serializer(data=request.data)
        if serializer_student.is_valid() :
            serializer_student.save()
        else :
            print("cannot validate student serializer")
            print(serializer_student.errors)
        
        serializer_ss = ss_serializer(data=request.data)
        if serializer_ss.is_valid() :
            serializer_ss.save()
        else : 
            print("cannot validate ss serializer")
            print(serializer_ss.errors)
            return  Response(serializer_ss.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer_student.data,status=status.HTTP_201_CREATED)

class nested_manange_withID(APIView) :
    def get_student_object(self,id) : #from stuid
        try : 
            query = Student.objects.get(student_ID=id)
        except : #school not exist
            return False
        return query
    
    def get_school_object(self,id) :#from schid
        try: 
            query = School.objects.get(school_name=id)
            
        except :#school not exist
            return False
        return query

    def get(self,request,schid=None,stuid=None):
        # query = Student_School.objects.filter(school_name=schid,student_ID=stuid)
        # print(query)
        school = self.get_school_object(schid)
        student = self.get_student_object(stuid)
        if school == False :
            school_out = list()
        else : school_out = school_serializer(school).data
        if student == False :
            student_out = list()
        else : student_out = student_serializer(student).data
        
        return Response(data={"school":school_out,"student":student_out},status=status.HTTP_200_OK)
    
    def delete(self,request,schid=None,stuid=None) :
        #delete student belong to school
        instance = Student_School.objects.filter(school_name=schid)
        for each in instance :
            student = Student.objects.get(student_ID=each.student_ID.student_ID)
            student.delete()

        try :
            school = self.get_school_object(schid)
            if school != False : school.delete()
            student = self.get_student_object(stuid)
            student.delete()
            return Response(data="Delete",status=status.HTTP_200_OK)
        except :
            return Response(data="Name is not valid",status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,schid=None,stuid=None) :
        school = self.get_school_object(schid)
        student = self.get_student_object(stuid)
        request.data['school_name'] = schid
        request.data['student_ID'] = stuid
        if school == False :
            out_school = "school name is not exist"
        else :
            serializer_school = school_serializer(school,data=request.data)
            if serializer_school.is_valid() :
                serializer_school.save()
            out_school = serializer_school.data
        if student == False :
            out_student = "student ID is not exist"
        else :
            serializer_student = student_serializer(student,data=request.data)
            if serializer_student.is_valid() :
                serializer_student.save()
            out_student = serializer_student.data
        
        return Response(data={"school":out_school,"student":out_student},status=status.HTTP_200_OK)