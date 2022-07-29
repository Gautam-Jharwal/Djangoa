from django.db import models

# Create your models here.

class Students(models.Model):
    Students_ID = models.CharField(max_length=100)
    Student_Name = models.CharField(max_length=100,default='SOME STRING')
    Student_Roll_no = models.IntegerField(default=0)
    Student_Phoneno = models.IntegerField(default=0)


class Teacher(models.Model):
    Teacher_ID = models.IntegerField(default='SOME STRING')
    Teacher_Name = models.CharField(max_length=100)
    Teacher_Phone = models.IntegerField(default=0)
    Course_ID = models.IntegerField(default=0)

class Courses(models.Model):
    Course_ID = models.IntegerField(default=0)
    Course_name = models.CharField(max_length=100,default='SOME STRING')
    Students_ID = models.CharField(max_length=100,default='SOME STRING')
    Course_Price = models.IntegerField(default=0)
    Course_Description = models.CharField(max_length=500,default='SOME STRING')

class Employee(models.Model):
    Employee_ID = models.IntegerField(default=0)
    Teacher_ID = models.IntegerField(default=0)
    Employee_Designation = models.CharField(max_length=200,default='SOME STRING')
    Employee_Salary = models.IntegerField(default=0)

class Assignment(models.Model):
    Assignment_ID = models.IntegerField(default=0)
    Teacher_ID = models.IntegerField(default=0)
    Student_Roll_no = models.IntegerField(default=0)

class Results(models.Model):
    Result_ID = models.IntegerField(default=0)
    Students_ID = models.CharField(max_length=100,default=0)
    Marks_Obtained = models.IntegerField(default=0)
    Remark = models.CharField(max_length=1000,default='SOME STRING')