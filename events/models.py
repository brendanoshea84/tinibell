from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    label = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=255, blank=False, null=False)
    image_1 = models.ImageField(upload_to="uploads/", blank=True, null=True)