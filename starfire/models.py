from django.db import models

# Create your models here.
class userlog(models.Model):
    b1=models.ImageField(upload_to="images/")
    b2=models.IntegerField(null=True)
class user(models.Model):
    usrname=models.CharField(max_length=30)
    usrpwd=models.CharField(max_length=5)
class userbill(models.Model):
    prdname=models.CharField(max_length=30)
    qty=models.IntegerField(max_length=500)
    date=models.DateField()
    place=models.CharField(max_length=30)
    email=models.EmailField()
    adress=models.CharField(max_length=50)
    phn=models.IntegerField(max_length=10)