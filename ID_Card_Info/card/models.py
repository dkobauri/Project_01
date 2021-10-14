from django.core import validators
from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from datetime import datetime, date
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

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
    Personal_N = models.CharField(max_length=11, null=True, unique=True)
    Date_Of_Birth = models.DateField(blank=True, null=True)
    Date_Of_Expiry = models.DateField(blank=True, null=True)
    Place_Of_Birth = models.CharField(max_length=50, null=True)
    Date_Of_Issue = models.DateField(blank=True, null=True)
    Issueing_Authority = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.First_Name

    def clean(self):
        symb = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', \
                '?', '/', '>', '.', '<', ',', '|', '"', ':', ';', '}', ']', '{', '[')
        for i in symb:
            if i in self.First_Name:
                raise ValidationError('In "First_Name" Field You Can Not Enter Following Simbols: \
                                        !, @, #, $, %, ^, &, *, (, ), _, +, =, ?, /, >, ., <, \
                                        ,, |, ", :, ;, }, ], {, [')
        for i in symb:
            if i in self.Last_Name:
                raise ValidationError('In "Last_Name" Field You Can Not Enter Following Simbols: \
                                        !, @, #, $, %, ^, &, *, (, ), _, +, =, ?, /, >, ., <, \
                                        ,, |, ", :, ;, }, ], {, [')
        if self.Personal_N.isdigit()==False:
            raise ValidationError('In "Personal_N" Field You Can Enter Only Numbers!')
        if self.Date_Of_Birth > date.today():
            raise ValidationError('In "Date_Of_Birth" Field You Can Not Select Future Date!')
        if self.Date_Of_Expiry <= self.Date_Of_Issue:
            raise ValidationError('Date In "Date_Of_Expiry" Field Can Not Be Less Or Equal To Date In "Date_Of_Issue" Field!')
        if self.Date_Of_Issue <= self.Date_Of_Birth:
            raise ValidationError('Date In "Date_Of_Issue" Field Can Not Be Less Or Equal To Date In "Date_Of_Birth" Field!')