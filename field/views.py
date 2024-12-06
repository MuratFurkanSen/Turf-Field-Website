from django.shortcuts import render, redirect
from .forms import FieldCreationForm
from .models import Field


# Create your views here.
def createField(request):
    print("Anan")
    if request.method == 'POST':
        print("Anan1")
        form = FieldCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print("Anan2")
            form.save()
            return redirect('/')

    form = FieldCreationForm()
    context = {
        'form' : form,
    }
    return render(request,'creation.html', context)


def fields(request):
    fields = Field.objects.all()
    context = {'fields': fields}
    return render(request,'fields.html', context)