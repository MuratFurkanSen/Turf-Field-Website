from django.contrib.auth.models import User

from field.models import Field
from django.db import models

# Create your models here.

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    users = models.ManyToManyField(User, related_name='reservations')
    field = models.OneToOneField(Field, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()

