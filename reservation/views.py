from idlelib.query import Query

from django.db.models import QuerySet
from django.http import JsonResponse
from django.shortcuts import render, redirect

from field.models import Field
from reservation.forms import ReservationForm


# Create your views here.


def create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST, user=request.user)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = ReservationForm(user=request.user)
    context = {'form': form}
    return render(request, 'createReservation.html', context)

def get_date_options(request):
    field_id = request.GET.get('field_id')
    field = Field.objects.get(pk=field_id)
    date_options = field.reservation_available_dates.all()

    return JsonResponse({'date_options': list(map(lambda x : str(x).split('+')[0], date_options))})

def reservation(request):
    return render(request, 'reservation.html')