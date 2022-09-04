from django.db import models


# Create your models here.


class SignUp(models.Model):
    Firstname = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    PhoneNumber = models.IntegerField()
    Email = models.CharField(max_length=50)
    Birthdate=models.DateField(null=True)
    password = models.CharField(max_length=50)
    ConfirmPassword = models.CharField(max_length=50)
