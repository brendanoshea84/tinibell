from django.db import models

# Create your models here.
class PickupLocation(models.Model):
    # Basic product information
    name = models.CharField(max_length=50, default="")
    label = models.CharField(max_length=50, default="location")
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False, default="Indianapolis")
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)