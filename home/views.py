from django.http import HttpResponse
from django.shortcuts import render

from reservation.models import Reservation
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
    if request.user.is_authenticated:
        user_teams = Team.objects.filter(members=request.user)
        reservations = Reservation.objects.filter(team__in=user_teams)
        context['reservations'] = reservations
        context['all_teams'] = user_teams
    return render(request, 'home.html', context)

def header_teams(request):
    if  request.user.is_authenticated:
        teams = {'teams': Team.objects.filter(members=request.user)[:3]}
        return teams
    return []


def test(request):
    anan = DateTimeEntry()
    anan.create_future_entries()
    return HttpResponse('Success 8')