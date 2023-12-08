from django.db import models


# Create your models here.
class Users(models.Model):
    nickname = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    profile = models.CharField(max_length=100,default="/static/favicon.ico")
    address = models.CharField(max_length=100, null=True)
    sex = models.CharField(max_length=2, null=True)
    registerdate = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=5, default="休闲娱乐")
