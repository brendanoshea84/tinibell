from django.db import models
from django.forms import BooleanField

class Product(models.Model):
    # Basic product information
    name = models.CharField(max_length=50, default="PRODUCT")
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)

    # Tools for admin to control site
    featured = models.BooleanField(default=False, blank=False, null=False)
    nmbr_remaining = models.IntegerField(blank=True, null=True)
    discontinued = models.BooleanField(default=False, blank=False, null=False)

    # For filtering by food sensitivity
    vegan = models.BooleanField(default=False, blank=False, null=False)
    gluten_free = models.BooleanField(default=False, blank=False, null=False)
    nut_free = models.BooleanField(default=False, blank=False, null=False)

    # Images
    image_1 = models.ImageField(upload_to="uploads/", blank=True, null=True)
    image_2 = models.ImageField(upload_to="uploads/", blank=True, null=True)
    image_3 = models.ImageField(upload_to="uploads/", blank=True, null=True)

    def __str__(self):
        return self.name