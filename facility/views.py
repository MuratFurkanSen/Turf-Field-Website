from django.shortcuts import render, redirect
from .forms import FacilityCreationForm

# Create your views here.
def facility(request):
    if request.method == "POST":
        form = FacilityCreationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': FacilityCreationForm()}
    return render(request, 'facility_creation.html', context=context)
