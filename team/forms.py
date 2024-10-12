from django import forms
from django.contrib.auth.models import User
from .models import Team


class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']

class TeamUpdateForm(forms.ModelForm):
    id = forms.IntegerField()
    class Meta:
        model = User
        fields = ['id']

