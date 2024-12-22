from django.shortcuts import render, redirect
from facility.models import Facility
from .forms import FieldCreationForm


# Create your views here.
def createField(request):
    if request.method == 'POST':
        form = FieldCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = FieldCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'field_creation.html', context)


def fields(request):
    facilities = Facility.objects.all()
    context = {'facilities' : facilities}
    return render(request,'fields.html', context)