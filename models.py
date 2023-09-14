from django.db import models

# Create your models here.
# attendance/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AttendanceRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=1, choices=(('P', 'Present'), ('A', 'Absent')))

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"
