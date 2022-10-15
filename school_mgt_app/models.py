from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from django.db.models import PROTECT


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Profile(models.Model):
    date_of_birth = models.DateField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class SchoolAdmin(models.Model):
    first_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    portfolio = models.CharField(max_length=255)
    grade_level = models.IntegerField()
    current_salary = models.DecimalField(max_digits=9, decimal_places=2)


class Student(models.Model):
    CLASS = (
        ('JSS 1', 'JSS 1'),
        ('JSS 2', 'JSS 2'),
        ('JSS 3', 'JSS 3'),
        ('SS 1', 'SS 1'),
        ('SS 2', 'SS 2'),
        ('SS 3', 'SS 3'),
    )
    first_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_of_birth = models.DateField(auto_now=True)
    student_class = models.CharField(max_length=255, choices=CLASS)


class Employee(models.Model):
    POST = (
        ('SUBJECT_TEACHER', 'Subject Teacher'),
        ('CLASS_TEACHER', 'Class Teacher'),
        ('CLASS_SUBJECT_TEACHER', 'Class Subject Teacher'),
    )

    first_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_of_birth = models.DateField(auto_now=True)
    date_of_appointed = models.DateField(auto_now=True)
    grade_level = models.IntegerField()
    current_salary = models.DecimalField(max_digits=9, decimal_places=2)
    post = models.CharField(max_length=255, choices=POST)
    subject = models.ForeignKey(Student, on_delete=models.PROTECT, related_name="+")
    student = models.ManyToManyField(Student)


class Result(models.Model):
    school_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    teacher_comment = models.CharField(max_length=255)
    student = models.OneToOneField(Student, on_delete=models.PROTECT)


class Subject(models.Model):
    GRADES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    )
    name = models.CharField(max_length=255)
    grade = models.CharField(max_length=50, choices=GRADES)
    result = models.ForeignKey(Result, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
