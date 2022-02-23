from django.db import models
from django.forms import BooleanField
from datetime import datetime


# Create your models here.
class PickupLocation(models.Model):
    # Basic product information
    name = models.CharField(max_length=50, default="")
    label = models.CharField(max_length=50, default="location")
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False, default="Indianapolis")
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    active = models.BooleanField(default=True, blank=False, null=False)
    description = models.CharField(max_length=50, default="", blank=True, null=True)

class Prices(models.Model):
    stuffed_pasta = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    pierogi = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)