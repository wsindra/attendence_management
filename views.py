from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect


# Create your views here.

def reg_fun(request):
    return render(request, 'register.html', {'data': ''})


def regdata_fun(request):
    userName = request.POST['tbname']
    Mail = request.POST['tbemail']
    Password = request.POST['tbpswrd']

    if User.objects.filter(Q(username=userName) | Q(email=Mail)).exists():
        return render(request, 'register.html', {'data': 'username,email and password is already exists'})
    else:
        u1 = User.objects.create_superuser(username=userName, email=Mail, password=Password)
        u1.save()
        return redirect('log')


def log_fun(request):
    return render(request, 'login.html', {'data': ''})



def logdata_fun(request):
    user_name = request.POST['tbuser']
    user_pswrd = request.POST['tbpswrd']
    user1 = authenticate(username=user_name, password=user_pswrd)
    if user1 is not None:
        if user1.is_superuser:
            login(request,user1)
            return redirect('home')
        else:
            return render(request, 'login.html', {'data': 'user is not superuser','res':False})
    else:
        return render(request, 'login.html', {'data': 'enter proper username and password','res':True})


def home_fun(request):
    return render(request,'home.html')

# attendance/views.py
from django.shortcuts import render, redirect
from .models import Student, AttendanceRecord
from datetime import date

@login_required
def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        student = Student.objects.create(name=name)
        return redirect('addstudent')
    return render(request, 'addstudent.html')

@login_required
def studentlist(request):
    student = Student.objects.all()
    return render(request,'studentlist.html',{'data':student})


@login_required
def mark_attendance(request):
    if request.method == 'POST':
        student_ids = request.POST.getlist('student_ids')
        status = request.POST['status']
        date_today = date.today()

        for student_id in student_ids:
            student = Student.objects.get(pk=student_id)
            AttendanceRecord.objects.create(student=student, date=date_today, status=status)

        return redirect('attendencelist')

    students = Student.objects.all()
    return render(request, 'markattendence.html', {'students': students})

def attendance_list(request):
    attendencerecord = AttendanceRecord.objects.all()
    return render(request, 'attendencelist.html', {'data': attendencerecord})


def delete_fun(request,id):
    students = Student.objects.get(id=id)
    students.delete()
    return redirect('studentlist')


def log_out_fun(request):
    logout(request)
    return redirect('log')