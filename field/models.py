from django.db import models

# Create your models here.
HOUR_CHOICES = tuple(
    (f'{str(i).zfill(2)}-{str(i+1).zfill(2)}', f'{str(i).zfill(2)}-{str(i+1).zfill(2)}') for i in range(24)
)


class Field(models.Model):
    # Field Related Info
    name = models.CharField(max_length=100)
    reservation_hours = models.CharField(max_length=255, choices=HOUR_CHOICES)  # "Starting Hours" 9,10,11
    is_have_shoes = models.BooleanField()

    # Address Related Info
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    indoor = models.CharField(max_length=100)
    maps_location = models.URLField()

    def __str__(self):
        return f"{self.id} - {self.name}"