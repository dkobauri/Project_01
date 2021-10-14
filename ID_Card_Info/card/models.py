from django.core import validators
from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from datetime import datetime, date
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

def only_int(value):
    if value.isdigit()==False:
        raise ValidationError('ID Number Contains Only Numbers!')

def date_of_birth(value):
    if value > date.today():
        raise ValidationError('You cannot select future date!')

# def date_of_issue(value):
    # if value < MinValueValidator(date_of_birth):
        # raise ValidationError('You cannot select future date!')

class Information(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    Photo = models.ImageField(null=True, blank=True)
    CARD_N = models.CharField(max_length=9, null=True, unique=True)
    First_Name = models.CharField(max_length=200, null=True)
    Last_Name = models.CharField(max_length=200, null=True)
    Citizenship = models.CharField(max_length=50, null=True)
    SEX = models.CharField(max_length=200, null=True, choices=GENDER)
    Personal_N = models.CharField(max_length=11, null=True, unique=True, validators=[only_int])
    Date_Of_Birth = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, validators=[date_of_birth])
    Date_Of_Expiry = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    Place_Of_Birth = models.CharField(max_length=50, null=True)
    Date_Of_Issue = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    Issueing_Authority = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.First_Name