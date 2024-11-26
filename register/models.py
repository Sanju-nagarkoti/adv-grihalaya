from django.db import models

# Create your models here.

class User(models.Model):
    userid=models.IntegerField()
    username=models.CharField(max_length=40)
    userpassword=models.CharField(max_length=40)
    useremail=models.CharField(max_length=40)

