from distutils.command.upload import upload
import email
from django.db import models
from sqlalchemy import false

# Create your models here.


class Destination(models.Model):
    name= models.CharField(max_length=100)
    # img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=false)

class loginModel(models.Model):
    userName=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=70)
    password=models.CharField(max_length=30)
    manager=models.BooleanField(default=false)
    