from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from facility.models import Facility
from field.models import Field
from reservation.models import Reservation
from team.models import Team


# Create your views here.

@login_required(login_url='login')
def create(request):
    field_id = int(request.GET.get('field_id'))
    team_id = int(request.GET.get('team_id'))
    year, month, day, hour = list(map(int,request.GET.get('selected_date').split("-")))

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
    facility_id = request.GET.get('facility_id')
    year, month, day = request.GET.get('selected_date').split("-")
    facility = Facility.objects.get(pk=facility_id)
    field_hour_options = []
    for field in facility.fields.all():
        raw_date_options = field.reservation_available_dates.filter(date__year=year, date__month=month, date__day=day)
        field_hour_options.append({f'{field.id},{field.name}':list(map(lambda x: str(x).split()[1].split(':')[0], raw_date_options))})
    print(field_hour_options)
    team_options = Team.objects.filter(captain=request.user)
    team_options = list(map(lambda team: f'{team.id},{team.name}', team_options))
    return JsonResponse({'fields_hour_options': field_hour_options, 'team_options': team_options})


def reservation(request):
    return render(request, 'fields.html')
