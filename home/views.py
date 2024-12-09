from dataclasses import field
from datetime import datetime

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from team.models import Team
from user.forms import UserRegistrationForm, UserLoginForm
from team.forms import TeamCreationForm

from field.models import DateTimeEntry, Field


def home(request):
    context = {'user': request.user}
    context['create_form'] = TeamCreationForm()
    if not request.user.is_authenticated:
        register_form = UserRegistrationForm()
        login_form = UserLoginForm()
        context['register_form'] = register_form
        context['login_form'] = login_form
    return render(request, 'home.html', context)

def header_teams(request):
    if  request.user.is_authenticated:
        teams = {'teams': Team.objects.filter(members=request.user)[:3]}
        return teams
    return []



def test(request):
    return render(request, 'abc.html', {})