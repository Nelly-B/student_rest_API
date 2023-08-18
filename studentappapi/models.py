from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, default='M')