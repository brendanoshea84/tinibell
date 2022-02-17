from django.db import models
from django.forms import BooleanField

# Create your models here.
"""
product image
name
description
price/lb
nmbr_remaining
discontinued
vegan
gluten_free
nut_free
"""

class Product(models.Model):
    # Basic product information
    name = models.CharField(max_length=50, default="PRODUCT")
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)

    # Tools for admin to control site
    featured = models.BooleanField(blank=False, null=False)
    nmbr_remaining = models.IntegerField(blank=True, null=True)
    discontinued = models.BooleanField(blank=False, null=False)

    # For filtering by food sensitivity
    vegan = models.BooleanField(blank=False, null=False)
    gluten_free = models.BooleanField(blank=False, null=False)
    nut_free = models.BooleanField(blank=False, null=False)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)