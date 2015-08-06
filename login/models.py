from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	username=models.OneToOneField(User)
	enrollmentnumber = models.IntegerField()
	GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    	)
	gender = models.CharField(max_length=6, blank=False, choices=GENDER_CHOICES)
	BRANCH_CHOICES = (
        ('CSE', 'Computer Science'),
        ('ECE', 'CElectronics'),
        ('EE', 'Electrical'),
        ('ME', 'Mechanical'),
        ('CHE', 'Chemical'),
        ('CE', 'Civil'),
        ('PHY', 'Physics'),
    	)
	branch = models.CharField(max_length=3, blank=False, choices=BRANCH_CHOICES)
	dob = models.DateField()
	about=models.CharField(max_length=500)

# Create your models here.
