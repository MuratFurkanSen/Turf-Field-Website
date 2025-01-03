from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile


class UserRegistrationForm(UserCreationForm):
    # Fields from UserProfile
    choices = (
        ("None", "Select Your Favorite Position"),
        ("X", "Doesn't Matter"),
        ("Back", "Back"),
        ("Forward", "Forward"),
        ("Middle", "Middle"),

    )
    full_name = forms.CharField(max_length=255, required=True,
                                widget=forms.TextInput(attrs={'class': 'signInput', 'placeholder': 'Name'}))
    birth_date = forms.DateField(required=True,
                                 widget=forms.DateInput(attrs={'class': 'signInput','type':'date', 'placeholder': 'Birth date'}))
    phone_number = forms.CharField(max_length=20, required=True,
                                   widget=forms.TextInput(attrs={'class': 'signInput', 'type':'tel','pattern':'[0-9]{3}-[0-9]{3}-[0-9]{4}', 'placeholder': 'Phone number'}))
    position = forms.ChoiceField(choices=choices, required=True,
                                 widget=forms.Select(attrs={'class': 'signInput', 'placeholder': 'Position'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'signInput', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'signInput', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        # Meta for the User model
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'signInput', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'signInput', 'placeholder': 'Email '}),
            'password1': forms.PasswordInput(attrs={'class': 'signInput', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'signInput', 'placeholder': 'Confirm Password'}),
        }

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

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'signInput', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'signInput', 'placeholder': 'Password'})
    )
    class Meta:
        model = User
        fields = ('username', 'password')


