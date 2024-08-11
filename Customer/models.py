from django.db import models

# Create your models here.

class CustomerUser(models.Model):
    Id=models.AutoField(primary_key=True)
    FullName=models.CharField(max_length=200, null=True)
    UserName=models.CharField(max_length=300, null=True)
    Password=models.CharField(null=True,max_length=200)
    IP=models.CharField(null=True,max_length=100,verbose_name="آیپی کابر")

class Customermessage(models.Model):
    Id = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=200)
    Email=models.EmailField(null=True,max_length=200,verbose_name="ایمیل")
    Issue=models.CharField(null=True,max_length=200)
    message = models.TextField(max_length=200, verbose_name="پیام")