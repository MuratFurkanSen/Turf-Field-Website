from django.contrib.auth.models import User
from django.db import models
from team.models import Team



# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    position = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=50)
    wallet_balance = models.IntegerField(default=0)
    friends = models.ManyToManyField(User, related_name='friends')

    def __str__(self):
        return f"{self.id}| " + self.user.username

class FriendInvite(models.Model):
    sender_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sender_user')
    recipient_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recipient_user')

class TeamInvite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='team')
    team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='invite')

