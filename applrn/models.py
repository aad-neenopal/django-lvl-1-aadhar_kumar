from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    age = models.PositiveSmallIntegerField()
    contact = PhoneNumberField()