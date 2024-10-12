from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    captain = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_captain')
    members = models.ManyToManyField(User, related_name='team_members')

    def __str__(self):
        return self.name
