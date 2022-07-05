from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=150)
    nationality = models.CharField(max_length=30)
    contact = models.IntegerField(null=True)
    dob = models.DateTimeField(null=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.user


class Booking_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(null=True)
    time = models.TimeField(null=True)
    number = models.IntegerField(null=True)

    def __str__(self):
        return self.user
