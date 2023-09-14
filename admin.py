from django.contrib import admin

from attendenceapp.models import Student, AttendanceRecord

# Register your models here.
admin.register(Student)
admin.register(AttendanceRecord)
