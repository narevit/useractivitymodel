from django.db import models

# Create your models here.

class Login(models.Model): 
    useremail = models.CharField(db_column='userEmail', unique=True, max_length=100) 
    name = models.CharField(max_length=100)
    password = models.CharField(db_column='Password', max_length=500)
    lastlogindate = models.DateTimeField(db_column='lastLoginDate', blank=True, null=True)
    createdon = models.DateTimeField(db_column='createdOn', blank=True, null=True)
    loginattempts = models.IntegerField(db_column='loginAttempts', blank=True, null=True)
    randomkey = models.CharField(max_length=45) 
