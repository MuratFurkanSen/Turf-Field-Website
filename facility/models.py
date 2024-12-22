from django.db import models

# Create your models here.

class Facility(models.Model):
    # Facility Related Info
    name = models.CharField(max_length=100)
    is_have_shoes = models.BooleanField()

    # Address Related Info
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    indoor = models.CharField(max_length=100)
    maps_location = models.CharField(max_length=100)

    def __str__(self):
        return self.name