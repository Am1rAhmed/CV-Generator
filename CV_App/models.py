from pyexpat import model
from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=250);
    phone = models.CharField(max_length=20);
    email = models.CharField(max_length= 250);
    school = models.CharField(max_length=250);
    degree = models.CharField(max_length=250);
    univercity = models.CharField(max_length=250);
    skill = models.CharField(max_length=2000);
    about_you = models.CharField(max_length=2000);
    Previous_works = models.CharField(max_length=2000);
