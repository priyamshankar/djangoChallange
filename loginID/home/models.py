from distutils.command.upload import upload
from django.db import models
from sqlalchemy import false

# Create your models here.


class Destination(models.Model):
    name= models.CharField(max_length=100)
    # img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=false)