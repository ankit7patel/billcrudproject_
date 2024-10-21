from django.db import models


class student(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_email = models.EmailField(unique=True)
    stu_contact = models.CharField(max_length=15)
    stu_password = models.CharField(max_length=100) 

   

class Query(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    query=models.TextField()
  
