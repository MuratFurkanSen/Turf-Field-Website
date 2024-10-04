from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    # Fields from UserProfile
    full_name = forms.CharField(max_length=255, required=True)
    birth_date = forms.DateField(required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    position = forms.CharField(max_length=255, required=True)

    class Meta:
        # Meta for the User model
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        # Save the User model
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        # Save the UserProfile model
        user_profile = UserProfile.objects.create(
            user=user,
            full_name=self.cleaned_data['full_name'],
            birth_date=self.cleaned_data['birth_date'],
            phone_number=self.cleaned_data['phone_number'],
            position=self.cleaned_data['position'],
        )
        if commit:
            user_profile.save()

        return user
