from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime
from django.utils import timezone
from django import forms

# Create your models here.

class beverage(models.Model):
    drinkcategory = (
        ('Whisky & Whiskey', 'Whisky & Whiskey'),
        ('Gin & Gin + Tonic', 'Gin & Gin + Tonic'),
        ('Cocktail', 'Cocktail'),
        ('Beer', 'Beer'),
        ('Coffee & Tea', 'Coffee & Tea'),
        ('Soda', 'Soda'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=drinkcategory)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class service(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class complementarydrink(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class barber(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

#test
TIME_CHOICES = (
    ("9 AM", "9 AM"),
    ("10 AM", "10 AM"),
    ("11 AM", "11 AM"),
    ("12 PM", "12 PM"),
    ("1 PM", "1 PM"),
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
    ("6 PM", "6 PM"),
    ("7 PM", "7 PM"),
)

class AppointmentNew(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(service, null=True, on_delete=models.SET_NULL)
    corresponding_drink = models.ForeignKey(complementarydrink, null=True, on_delete=models.SET_NULL, blank=True)
    chosen_barber = models.ForeignKey(barber, null=True, on_delete=models.CASCADE)
    additional_drinks = models.ManyToManyField(beverage, blank=True)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="9 AM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | Day: {self.day} | Time: {self.time}"