from django.shortcuts import render, redirect
from .forms import FieldCreationForm
from .models import Field


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
    fields = Field.objects.all()
    context = {'fields': fields}
    return render(request,'fields.html', context)