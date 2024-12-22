from django import forms

from facility.models import Facility
from .models import Field

HOUR_CHOICES = tuple(
    (f'{str(i).zfill(2)}-{str(i + 1).zfill(2)}', f'{str(i).zfill(2)}-{str(i + 1).zfill(2)}') for i in range(24)
)
province_choices = (
    ('1', 'Adana'),
)
district_choices = (
    ('1', 'Seyhan'),
)
neighborhood_choices = (
    ('1', 'Ahmet Remzi Yüreğir'),
)
street_choices = (
    ('1', '59004'),
)
building_choices = (
    ('1', '5'),
)
indoor_choices = (
    ('1', '1'),
)


class FieldCreationForm(forms.ModelForm):
    mon_time_slots = forms.MultipleChoiceField(
        widget=forms.SelectMultiple,
        choices=HOUR_CHOICES,
        label='Monday Time Slots',
    )
    tue_time_slots = forms.MultipleChoiceField(
        widget=forms.SelectMultiple,
        choices=HOUR_CHOICES,
        label='Tuesday Time Slots',
    )
    wed_time_slots = forms.MultipleChoiceField(
        widget=forms.SelectMultiple,
        choices=HOUR_CHOICES,
        label='Wednesday Time Slots',
    )
    thu_time_slots = forms.MultipleChoiceField(
        widget=forms.SelectMultiple,
        choices=HOUR_CHOICES,
        label='Thursday Time Slots',
    )
    fri_time_slots = forms.MultipleChoiceField(
        widget=forms.SelectMultiple,
        choices=HOUR_CHOICES,
        label='Friday Time Slots',
    )
    sat_time_slots = forms.MultipleChoiceField(
        widget=forms.SelectMultiple,
        choices=HOUR_CHOICES,
        label='Saturday Time Slots',
    )
    sun_time_slots = forms.MultipleChoiceField(
        widget=forms.SelectMultiple,
        choices=HOUR_CHOICES,
        label='Sunday Time Slots',
    )

    class Meta:
        model = Field
        fields = [
            # Field Info
            'name', 'belonged_facility',
            # Schedule Info
            'mon_time_slots', 'tue_time_slots', 'wed_time_slots',
            'thu_time_slots', 'fri_time_slots', 'sat_time_slots', 'sun_time_slots']
        widgets = {}

    def save(self, commit=True):
        field = super(FieldCreationForm, self).save(commit=False)
        field.schedule['Mon'] = ','.join(slot.split('-')[0] for slot in self.cleaned_data['mon_time_slots'])
        field.schedule['Tue'] = ','.join(slot.split('-')[0] for slot in self.cleaned_data['tue_time_slots'])
        field.schedule['Wed'] = ','.join(slot.split('-')[0] for slot in self.cleaned_data['wed_time_slots'])
        field.schedule['Thu'] = ','.join(slot.split('-')[0] for slot in self.cleaned_data['thu_time_slots'])
        field.schedule['Fri'] = ','.join(slot.split('-')[0] for slot in self.cleaned_data['fri_time_slots'])
        field.schedule['Sat'] = ','.join(slot.split('-')[0] for slot in self.cleaned_data['sat_time_slots'])
        field.schedule['Sun'] = ','.join(slot.split('-')[0] for slot in self.cleaned_data['sun_time_slots'])

        if commit:
            field.save()
        return field
