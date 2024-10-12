from django.contrib.auth.models import User

from field.models import Field
from team.models import Team
from django.db import models

# Create your models here.

class Reservation(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()

    def __str__(self):
        return str(self.reservation_date)

