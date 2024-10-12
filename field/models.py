from django.db import models

# Create your models here.

class Field(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    open_address = models.CharField(max_length=100)
    maps_location = models.URLField()
    reservation_hours = models.CharField(max_length=100) # "Starting Hours" 9,10,11
    is_have_shoes = models.BooleanField()

    def __str__(self):
        return f"{self.id} - {self.name}"