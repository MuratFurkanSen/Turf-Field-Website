from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from field.models import Field
from reservation.forms import ReservationForm
from reservation.models import Reservation
from team.models import Team


# Create your views here.

@login_required(login_url='login')
def create(request):
    field_id = int(request.GET.get('field_id'))
    team_id = int(request.GET.get('team_id'))
    year, month, day, hour = list(map(int,request.GET.get('selected_date').split("-")))
    print(field_id,team_id, month, day, hour)

    selected_date = datetime(year, month, day, hour,0,0)
    if not Field.objects.filter(id=field_id).exists():
        return HttpResponse("Invalid Query")
    if not Team.objects.filter(id=team_id).exists():
        return HttpResponse("Invalid Query")
    field = Field.objects.get(id=field_id)
    team = Team.objects.get(id=team_id)
    if request.user != team.captain:
        return HttpResponse("You are Not the Captain of Selected Team")
    if not field.reservation_available_dates.filter(date=selected_date).exists():
        return HttpResponse("Invalid Query")
    field.reservation_available_dates.filter(date=selected_date)[0].delete()
    Reservation.objects.create(field=field, team=team, reservation_date=selected_date).save()
    return redirect("/")




def get_reservation_options(request):
    field_id = request.GET.get('field_id')
    year, month, day = request.GET.get('selected_date').split("-")
    print(year, month, day, sep='-')
    field = Field.objects.get(pk=field_id)

    date_options = field.reservation_available_dates.filter(date__year=year, date__month=month, date__day=day)
    print(date_options)
    date_options = list(map(lambda x: str(x).split()[1].split(':')[0], date_options))
    print(date_options)
    return JsonResponse({'date_options': date_options})


def reservation(request):
    return render(request, 'fields.html')
