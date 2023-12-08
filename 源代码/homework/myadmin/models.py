from django.db import models


# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    pic = models.CharField(max_length=150, default="/static/favicon.ico")
    pub_date = models.DateField(auto_now_add=True)
    price = models.FloatField()
    publisher = models.CharField(max_length=100)
    abstract = models.TextField()
    type = models.CharField(max_length=10, null=True)


class Admin_Users(models.Model):
    nickname = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=100)
    profile = models.CharField(max_length=100, default="/static/favicon.ico")
    sex = models.CharField(max_length=1, null=True)
    registerdate = models.DateField(auto_now_add=True)


class Types(models.Model):
    name = models.CharField(max_length=20)