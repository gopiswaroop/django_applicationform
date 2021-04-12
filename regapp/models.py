from django.db import models


# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=30)
    fathername = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    contact = models.IntegerField()
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
