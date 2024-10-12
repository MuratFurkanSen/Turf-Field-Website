from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    position = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=50)
    wallet_balance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}| " + self.user.username
