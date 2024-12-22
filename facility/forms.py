from django import forms
from .models import *

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


class FacilityCreationForm(forms.ModelForm):
    province_slots = forms.ChoiceField(
        widget=forms.Select,
        choices=province_choices,
        label='Province Slots',
    )
    district_slots = forms.ChoiceField(
        widget=forms.Select,
        choices=district_choices,
        label='District Slots',
    )
    neighborhood_slots = forms.ChoiceField(
        widget=forms.Select,
        choices=neighborhood_choices,
        label='Neighborhood Slots',
    )
    street_slots = forms.ChoiceField(
        widget=forms.Select,
        choices=street_choices,
        label='Street Slots',
    )
    building_slots = forms.ChoiceField(
        widget=forms.Select,
        choices=building_choices,
        label='Building Slots',
    )
    indoor_slots = forms.ChoiceField(
        widget=forms.Select,
        choices=indoor_choices,
        label='Indoor Slots',
    )

    class Meta:
        model = Facility
        fields = [
            # General Info
            'name', 'is_have_shoes',
            # Address Info
            'province_slots', 'district_slots', 'neighborhood_slots',
            'street_slots', 'building_slots', 'indoor_slots',
            'maps_location', ]
        widgets = {}

    def save(self, commit=True):
        facility = super(FacilityCreationForm, self).save(commit=False)
        facility.province = self.cleaned_data['province_slots']
        facility.district = self.cleaned_data['district_slots']
        facility.neighborhood = self.cleaned_data['neighborhood_slots']
        facility.street = self.cleaned_data['street_slots']
        facility.building = self.cleaned_data['building_slots']
        facility.indoor = self.cleaned_data['indoor_slots']

        if commit:
            facility.save()
        return facility
