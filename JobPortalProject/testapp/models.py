from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phno = models.IntegerField()

class BloreJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phno = models.IntegerField()

class PuneJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phno = models.IntegerField()

class ChennaiJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phno = models.IntegerField()
