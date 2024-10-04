from django.db import models

# Create your models here.

class Field(models.Model):
    field_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    open_address = models.CharField(max_length=100)
    maps_location = models.CharField(max_length=100)
    reservation_hours = models.CharField(max_length=100) # "Starting Hours" 9,10,11
    shoes = models.CharField(max_length=100) # "Size:Count" 40:6,41:9,42:9

    def __str__(self):
        return f"{self.id} - {self.name}"