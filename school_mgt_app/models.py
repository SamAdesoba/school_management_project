import email

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

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


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_of_birth = models.DateField(auto_now=True)


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_of_birth = models.DateField(auto_now=True)
    date_of_appointed = models.DateField(auto_now=True)


class Result(models.Model):
    school_name = models.CharField(max_length=255)
    grade = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
