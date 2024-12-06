from django import forms

from .models import Reservation
from field.models import Field, DateTimeEntry
from team.models import Team


class ReservationForm(forms.ModelForm):
    teams = forms.ModelChoiceField(
        queryset=Team.objects.none(),
        empty_label="Select a Team",
    )
    date_options = forms.ModelChoiceField(
        queryset=Field.objects.none(),
        empty_label="Select a Reservation Date",
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.field = Field.objects.get(id=2)
        self.fields['teams'].queryset = Team.objects.filter(captain_id=self.user.id).all()
        self.fields['date_options'].queryset = self.field.reservation_available_dates.all()

    class Meta:
        model = Reservation
        fields = ['teams', 'date_options']
        widgets = {}

    def save(self, commit=True):
        reservation = super(ReservationForm, self).save(commit=False)
        reservation.field = self.field
        reservation.team = self.cleaned_data['teams']
        reservation.reservation_date = self.cleaned_data['date_options'].date
        if commit:
            reservation.save()
