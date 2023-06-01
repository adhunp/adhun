from django.db import models

# Create your models here.

class Student(models.Model):
    sname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20 )
    semail = models.CharField(max_length = 20)
    sdob = models.CharField(max_length = 20)
    sphone = models.BigIntegerField()
    # parent_name = models.CharField(max_length = 20)
    address1=models.CharField(max_length = 20 )
    address2=models.CharField(max_length = 20 )
    password = models.CharField(max_length=30)