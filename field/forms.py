from django import forms
from .models import Field

HOUR_CHOICES = tuple(
    (f'{str(i).zfill(2)}-{str(i + 1).zfill(2)}', f'{str(i).zfill(2)}-{str(i + 1).zfill(2)}') for i in range(24)
)
class FieldCreationForm(forms.ModelForm):
    time_slots = forms.MultipleChoiceField(
        widget=forms.SelectMultiple,
        choices=HOUR_CHOICES,
        label='Time Slots',
    )
    class Meta:
        model = Field
        fields = "__all__"
        widgets = {

        }
