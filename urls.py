from django.urls import path

from attendenceapp import views

urlpatterns=[
    path('',views.log_fun,name='log'),
    path('logindata', views.logdata_fun),
    path('Reg',views.reg_fun,name='Reg'),
    path('read',views.regdata_fun),
    path('log',views.log_fun,name='log_fun'),
    path('home', views.home_fun, name='home'),
    path('addstudent', views.add_student, name='addstudent'),
    path('studentlist',views.studentlist,name='studentlist'),
    path('markattendence', views.mark_attendance, name='markattendence'),
    path('attendencelist', views.attendance_list, name='attendencelist'),
    path('delete/<int:id>',views.delete_fun,name='delete'),
    path('log_out',views.log_out_fun,name='log_out')

]

