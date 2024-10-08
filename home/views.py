from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from user.forms import UserRegistrationForm, UserLoginForm


# Create your views here.
def home(request):
    context = {'user': request.user}
    if not request.user.is_authenticated:
        register_form = UserRegistrationForm()
        login_form = UserLoginForm()
        context['register_form'] = register_form
        context['login_form'] = login_form
    return render(request, 'home.html', context)