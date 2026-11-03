from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200,null=True)
    age=models.CharField(null=True)
    phone=models.CharField(null=True)
    nessage=models.CharField(null=True)