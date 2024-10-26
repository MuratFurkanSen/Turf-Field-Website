from django.shortcuts import render, redirect
from .forms import FieldCreationForm

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
