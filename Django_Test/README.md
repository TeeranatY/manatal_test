# Django Test
## Requirement
    - python(version > 3.5)
    - asgiref(version 3.2.7)
    - djangorestframework(version 3.11.0)
    - psycopg2(version 2.8.5)
    - pytz(version 2020.1)
    - sqlparse(version 0.3.1)
## Installing
`In the Django Test directory create environment`
```
    pipenv install -r path/to/requirements.txt
```
## Start server
`Run run.bat to start a server`

## Database
In this project I use postgresql 
### Table
   - Student
      - student_ID (primary key, varchar(20))
      - firstname (varchar(20), not null)
      - lastname (varchar(20), not null)
   - School
     - school_name (primary key, varchar(20))
     - max_student_number (integer)
   - Student_School
     - student_ID (foreign key to Student)
     - school_name (foreign key to School)

## Description
### 1.Get, Post Student 
`Endpoint : ` **/students/** `
 - Get all student in Student table
   - response : all student in Student table
   - response : HTTP_STATUS 400 if student is empty
 - Post Student
    - request : **{"firstname":$FIRSTNAME,"lastname": $LASTNAME,"school_name": $SCHOOLNAME}**
    - response : HTTP_STATUS 201
    - response : HTTP_STATUS 400 if student already exist, school not exist, and the number of student are exceeding max_student_number
### 2.Get, Post School 
`Endpoint : ` **/schools/** `
 - Get all school in School table
   - response : all school in School table
   - response : HTTP_STATUS 400 if student is empty
 - Post School
   - request :**{"school_name" : $SCHOOLNAME , "max_student_number": $NUMBER}**
   - response : HTTP_STATUS 201
### 3.Get, Put, Delete Student to database given student_id
`Endpoint : ` **/students/:id** `
 - Get 
   - response : student in Student table with student_ID = id
   - response : HTTP_STATUS 400 if id is not exist
 - Put Student
   - request :**{"firstname":$FIRSTNAME,"lastname": $LASTNAME}**
   - response : HTTP_STATUS 200
   - response : HTTP_STATUS 400 if student_id is not exist
 - Delete student in Student table
   - response : HTTP_STATUS 400 if id is not exist

### 4.Get, Post School  given school_name 
`Endpoint : ` **/schools/:id** `
 - Get 
   - response : school with school_name = id
   - response : HTTP_STATUS 400 if school_name is not exist
 - Put 
   - request :**{"firstname": $FIRSTNAME,"lastname": $LASTNAME}**
   - response : edited data , HTTP_STATUS 200
   - response : HTTP_STATUS 400 if school_name is not exist
 - Delete 
   - response : HTTP_STATUS 200
   - response : HTTP_STATUS 400 if school_name is not exist

### 5.Get, Post Student given school_name 
`Endpoint : ` **/schools/:schid/students/** `
 - Get 
   - response :all student that belong to school_name
   - response : HTTP_STATUS 400 if school_name is not exist
 - Post add student to given school_name
   - request :**{"firstname": $FIRSTNAME,"lastname": $LASTNAME}**
   - response : HTTP_STATUS_201
   - response : HTTP_STATUS 400 if student already exist, school not exist, and the number of student are exceeding max_student_number
### 6.Get, Post School to database given id
`Endpoint : ` **/schools/:schid/students/:stuid** `
 - Get 
   - response : school and student which school_name = schid, and student_ID = stuid 
 - Put 
   - request :**{"firstname": $FIRSTNAME,"lastname": $LASTNAME,"max_student_number": $NUMBER}**
   - response : edited data ,HTTP_STATUS 200
   - response : HTTP_STATUS 400 if school_name or student_ID is not exist
 - Delete 
   - response : HTTP_STATUS 200
   - response : HTTP_STATUS 400 if school_name or student_ID is not exist