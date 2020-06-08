from django.urls import path,re_path
from school_manager.view  import manage_school,manage_student,manage_student_withID,manage_school_withID,nested_manage_school,nested_manange_withID

urlpatterns = [
    # path('',index),
    path('students/',manage_student.as_view()),
    path('students/<str:id>/',manage_student_withID.as_view()) ,
    path('schools/',manage_school.as_view()),
    path('schools/<str:id>/',manage_school_withID.as_view()),
    path('schools/<str:id>/students/',nested_manage_school.as_view()),
    path('schools/<str:schid>/students/<str:stuid>/',nested_manange_withID.as_view())
    # path('schools/<str:id>/students/<str:id>',nested_school.as_view())
    # path('/schools/:id')
]