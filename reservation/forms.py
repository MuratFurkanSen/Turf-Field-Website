from datetime import datetime
import re
from django import forms
from django.utils.timezone import override

from .models import Reservation
from field.models import Field
from team.models import Team


class ReservationForm(forms.ModelForm):
    fields = forms.ModelChoiceField(
        queryset=Field.objects.all(),
        empty_label="Select a category",
    )
    teams = forms.ModelChoiceField(
        queryset=Team.objects.none(),
        empty_label="Select a team",
    )
    choices = [(datetime(2024, 11, 10, 0, 0, 0), 'Anan'),]
    date_options = forms.CharField(max_length=100,widget=forms.Select(choices=[]))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['teams'].queryset = Team.objects.filter(captain_id=self.user.id).all()

    class Meta:
        model = Reservation
        fields = ['fields', 'teams', 'date_options']
        widgets = {}

    def save(self, commit=True):
        reservation = super(ReservationForm, self).save(commit=False)
        reservation.team = self.cleaned_data['teams']
        reservation.field = self.cleaned_data['fields']
        date = datetime(*list(map(int, re.split('[ :-]', self.cleaned_data['date_options']))))
        reservation.reservation_date = date
        if commit:
            reservation.save()
